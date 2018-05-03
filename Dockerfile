# Usage (given build times depend on machine):
#
#    Build SMALL image (no cache; ~20MB, time for build=rebuild = ~360s):
#    docker build --squash="true" -t clubhouse:latest .
#
#    Build FAST (rebuild) image (cache; >280MB, build time ~360s, rebuild time ~80s):
#    docker build -t clubhouse .
#
#    Clean (remove intermidiet images):
#    docker rmi -f $(docker images -f "dangling=true" -q)
#
#    Run image (on localhost:8080):
#    docker run --name clubhouse -p 8080:80 clubhouse &
#
#    Run image as virtual host (read more: https://github.com/jwilder/nginx-proxy):
#    docker run -e VIRTUAL_HOST=clubhouse.your-domain.com --name clubhouse clubhouse &

FROM python:3.6-slim

ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8' LANGUAGE='en_US.UTF-8'

# install
RUN set -ex; \
    \
    echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen; \
    apt-get update -qqy; \
    apt-get -qqy install --no-install-recommends \
        bash \
        libssl-dev \
        locales \
        ca-certificates \
    ; \
    /usr/sbin/update-locale LANG='en_US.UTF-8'; \
    update-ca-certificates; \
    apt-get autoremove -y && apt-get clean && apt-get autoclean; \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* /tmp; \
    mkdir -p /opt/app; \
    pip install 'pip>=9,<10' setuptools pipenv

# install pip ( in separate dir due to docker cache)
ADD setup.py Pipfile /opt/app/
RUN cd /opt/app && pipenv install --dev --skip-lock --system

WORKDIR /opt/app/clubhouse
ADD  . /opt/app/clubhouse/
VOLUME /opt/app/clubhouse

# this is for virtual host purposes
EXPOSE 3141 3142 8000
CMD ["python"]
