"""
Parses https://clubhouse.io/api/rest/v2/ and generates a JSON payload
of their resources that can be used as basis of a client library.

"""
import argparse
import logging
import sys
import re
from typing import Dict
from collections import OrderedDict, deque

from lxml import html
from unidecode import unidecode
from jinja2 import BaseLoader, Environment

import dag


_jinja_env = Environment(loader=BaseLoader(), trim_blocks=True, lstrip_blocks=True)
logger = logging.getLogger(__name__)


ENCODINGS_WITH_SMART_QUOTES = [
    "windows-1252",
    "iso-8859-1",
    "iso-8859-2",
]


def conf_logging(cli_arguments):
    logger = logging.getLogger()
    sfmt = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
    formatter = logging.Formatter(sfmt)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, cli_arguments.log_level.upper()))


def add_logging_options(options):
    options.add_argument(
        '-l', '--log-level',
        default='INFO',
        help='Set the logging level',
        choices=[
            'debug',
            'info',
            'warn',
            'warning',
            'error',
            'critical',
            'fatal',
            ],
        )
    return options


def add_options(options):
    options.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                         default=sys.stdin,
                         help="path to file to parse, defaults to stdin")
    options.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                         default=sys.stdout,
                         help="path to dump the output, defaults to stdout")
    return options


def execute(parser):
    parser = add_options(parser)
    args = parser.parse_args()
    conf_logging(args)

    parsed = parse(html.parse(args.infile))
    munged = munge(parsed)
    rendered = build(munged)
    with args.outfile as f:
        f.write(rendered)


def parse(tree):
    resources = tree.xpath('//h1[text()="Resources"]/following-sibling::h2')
    tables = tree.xpath('//h1[text()="Resources"]/following-sibling::table')
    logger.debug('resources: %s', resources)
    parsed = {}
    for resource, rawtable in zip(resources, tables):
        resource_name = resource.xpath('string(.)')
        logger.info('resource: %s', resource_name)
        parsed[resource_name] = extract(rawtable)

    logger.debug(parsed)
    return parsed


def extract(table):
    headers = table.xpath('thead/tr/th/text()')
    fields = table.xpath('./tbody/tr/td[strong]')
    descriptions = table.xpath('./tbody/tr/td[not(strong)]')
    logger.debug('headers: %s', [h for h in headers])
    extracted_fields = [
        (h.findtext('strong'), h.xpath('string(./span)'))
        for h in fields
    ]
    extracted_descriptions = []
    for h in descriptions:
        asbytes = bytes(h.text, ENCODINGS_WITH_SMART_QUOTES[0])
        extracted_descriptions.append(unidecode(str(asbytes, ENCODINGS_WITH_SMART_QUOTES[2])))

    logger.debug('fields: %s', extracted_fields)
    logger.debug('descriptions: %s', extracted_descriptions)
    rv = {f[0]: {"type": f[1], "description": d, "args": ''}
          for f, d in zip(extracted_fields, extracted_descriptions)}
    logger.debug(rv)
    return rv


def munge(datablob: Dict[str, Dict]) -> Dict[str, Dict]:
    #: searches for data between () or [] .. also matches [)..
    nested = re.compile(r'(?:\[|\()(?P<inside>.+)(?:\]|\))')

    def has_nested(type_):
        return any(('Array' in type_, type_ in datablob,))

    graph = dag.DAG()

    for resource_name, resource in datablob.items():

        graph.add_node_if_not_exists(resource_name)

        for details in resource.values():
            if 'or null' in details['type']:
                details['type'] = details['type'].split(' ')[0]
                details['args'] = 'allow_none=True'
            elif 'Enum' in details['type']:
                choices = nested.search(details['type']).group(1).split(',')
                details['type'] = 'String'
                details['args'] = 'validate=validate.OneOf({0})'.format(
                    ', '.join(['"{0}"'.format(c.strip()) for c in choices])
                )

            if not has_nested(details['type']):
                continue

            fieldtype = details['type']
            logger.info('%s: %s\n%s', resource_name, fieldtype, details)
            if 'Array' in fieldtype:
                details['args'] = ', many=True'
                fieldtype = nested.search(fieldtype).group(1)

            if fieldtype not in datablob:
                # if the field type is not part of the resources, then
                # we will use marshmallow default fields
                details['type'] = 'fields.' + fieldtype
                continue

            graph.add_node_if_not_exists(fieldtype)
            if fieldtype == resource_name:
                # marshmallow self-nesting schema
                logger.info(
                    'self referential cycle detected for %s on %s',
                    resource_name,
                    fieldtype
                )
                fieldtype = '"self"'
            else:
                logger.info('---- %s: ', fieldtype)
                graph.add_edge(fieldtype, resource_name)

            details['type'] = fieldtype
            details['args'] = ', many=False'


    ob = OrderedDict()
    for r in graph.topological_sort():
        logger.info(r)
        ob[r] = datablob[r]
    return ob


def build(datablob: Dict[str, Dict]):
    _template = """\
from marshmallow import Schema, fields, pprint, validate

{% for resource_name, resource in resources.items(): %}
class {{ resource_name }}(Schema):
{% for field, details in resource.items() %}
    {{ '#: ' ~ details.description | wordwrap(73) | replace('\n', '\n#: ') | indent }}
{# parses the types and understands how to map to schemas #}

{%- if 'many' is in(details.args) %}
    {{ field }} = fields.Nested({{details.type}}{{details.args}})
{% else %}
    {{ field }} = fields.{{details.type}}({{details.args}})
{% endif %}

{% endfor %}
{% endfor %}
"""
    rtemplate = _jinja_env.from_string(_template)
    _rendered = rtemplate.render(resources=datablob)
    logger.debug('%s: ', _rendered)
    return _rendered


def main():
    option_parser = argparse.ArgumentParser()
    option_parser = add_logging_options(option_parser)
    execute(option_parser)


if __name__ == '__main__':
    main()
