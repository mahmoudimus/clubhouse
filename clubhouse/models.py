from marshmallow import Schema, fields, pprint, validate


class PullRequest(Schema):
    #: The ID of the branch for the particular pull request.
    branch_id = fields.Integer()

    #: True/False boolean indicating whether the GitHub pull request has been
    #: closed.
    closed = fields.Boolean()

    #: The time/date the pull request was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique ID associated with the pull request in Clubhouse.
    id = fields.Integer()

    #: Number of lines added in the pull request, according to GitHub.
    num_added = fields.Integer()

    #: The number of commits on the pull request.
    num_commits = fields.Integer()

    #: Number of lines modified in the pull request, according to GitHub.
    num_modified = fields.Integer()

    #: Number of lines removed in the pull request, according to GitHub.
    num_removed = fields.Integer()

    #: The pull requests unique number ID in GitHub.
    number = fields.Integer()

    #: The ID of the target branch for the particular pull request.
    target_branch_id = fields.Integer()

    #: The title of the pull request.
    title = fields.String()

    #: The time/date the pull request was created.
    updated_at = fields.Date()

    #: The URL for the pull request.
    url = fields.String()

class Category(Schema):
    #: A true/false boolean indicating if the Category has been archived.
    archived = fields.Boolean()

    #: The hex color to be displayed with the Category (for example, #ff0000).
    color = fields.String(allow_none=True)

    #: The time/date that the Category was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Category
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: The unique ID of the Category.
    id = fields.Integer()

    #: The name of the Category.
    name = fields.String()

    #: The type of entity this Category is associated with; currently Milestone
    #: is the only type of Category.
    type = fields.String()

    #: The time/date that the Category was updated.
    updated_at = fields.Date()

class Comment(Schema):
    #: The unique ID of the Member who is the Comments author.
    author_id = fields.UUID(allow_none=True)

    #: The time/date when the Comment was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Comment
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: The unique ID of the Comment.
    id = fields.Integer()

    #: The unique IDs of the Member who are mentioned in the Comment.
    mention_ids = fields.Nested(fields.UUID, many=True)

    #: The Comments numerical position in the list from oldest to newest.
    position = fields.Integer()

    #: The ID of the Story on which the Comment appears.
    story_id = fields.Integer()

    #: The text of the Comment.
    text = fields.String()

    #: The time/date when the Comment was updated.
    updated_at = fields.Date(allow_none=True)

class Identity(Schema):
    #: A string description of this resource.
    entity_type = fields.String()

    #: This is your login in GitHub.
    name = fields.String(allow_none=True)

    #: The type of Identity; currently only type is github.
    type = fields.String(allow_none=True)

class CreateCategoryParams(Schema):
    #: The hex color to be displayed with the Category (for example, #ff0000).
    color = fields.String()

    #: This field can be set to another unique ID. In the case that the Category
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String()

    #: The name of the Category.
    name = fields.String()

class CreateCommentParams(Schema):
    #: The unique ID of the Member who is the Comments author.
    author_id = fields.UUID()

    #: The time/date when the Comment was created.
    created_at = fields.Date()

    #: An optional user-defined ID perhaps associating Comment with an outside
    #: tool.
    external_id = fields.String()

    #: The text of the Comment.
    text = fields.String()

    #: The time/date when the Comment was updated.
    updated_at = fields.Date()

class CreateLabelParams(Schema):
    #: The hex color to be displayed with the Label (for example, #ff0000).
    color = fields.String()

    #: An optional user-defined ID perhaps associating the Epic with an outside
    #: tool.
    external_id = fields.String()

    #: The Label name.
    name = fields.String()

class CreateStoryLinkParams(Schema):
    #: The unique ID of the Story defined as object.
    object_id = fields.Integer()

    #: The unique ID of the Story defined as subject.
    subject_id = fields.Integer()

    #: How the subject Story acts on the object Story.  This can be blocks,
    #: duplicates, or relates to.
    verb = fields.String(validate=validate.OneOf("blocks", "duplicates", "relates to"))

class CreateTaskParams(Schema):
    #: A true/false boolean indicating whether the Task is complete.
    complete = fields.Boolean()

    #: The time/date that the Task was created.
    created_at = fields.Date()

    #: The Task description.
    description = fields.String()

    #: An optional user-defined ID perhaps associating Task with an outside
    #: tool.
    external_id = fields.String()

    #: An array of unique IDs associated with the Members that own the Task.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: The time/date that the Task was updated.
    updated_at = fields.Date()

class ThreadedComment(Schema):
    #: The unique ID of the Member that authored the Comment.
    author_id = fields.UUID()

    #: A nested array of threaded comments.
    comments = fields.Nested("self", many=False)

    #: The time/date the Comment was created.
    created_at = fields.Date()

    #: True/false boolean indicating whether the Comment is deleted.
    deleted = fields.Boolean()

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Comment
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: The unique ID of the Comment.
    id = fields.Integer()

    #: An array of Member IDs that have been mentioned in this Comment
    mention_ids = fields.Nested(fields.UUID, many=True)

    #: The text of the Comment.
    text = fields.String()

    #: The time/date the Comment was updated.
    updated_at = fields.Date()

class EpicStats(Schema):
    #: The date of the last update of a Story in this Epic.
    last_story_update = fields.Date(allow_none=True)

    #: The total number of points in this Epic.
    num_points = fields.Integer()

    #: The total number of completed points in this Epic.
    num_points_done = fields.Integer()

    #: The total number of started points in this Epic.
    num_points_started = fields.Integer()

    #: The total number of unstarted points in this Epic.
    num_points_unstarted = fields.Integer()

    #: The total number of done Stories in this Epic.
    num_stories_done = fields.Integer()

    #: The total number of started Stories in this Epic.
    num_stories_started = fields.Integer()

    #: The total number of Stories with no point estimate.
    num_stories_unestimated = fields.Integer()

    #: The total number of unstarted Stories in this Epic.
    num_stories_unstarted = fields.Integer()

class File(Schema):
    #: Free form string corresponding to a text or image file.
    content_type = fields.String()

    #: The time/date that the file was created.
    created_at = fields.Date()

    #: The description of the file.
    description = fields.String(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the File has
    #: been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: The name assigned to the file in Clubhouse upon upload.
    filename = fields.String()

    #: The unique ID for the file.
    id = fields.Integer()

    #: The unique IDs of the Members who are mentioned in the file description.
    mention_ids = fields.Nested(fields.UUID, many=True)

    #: The optional User-specified name of the file.
    name = fields.String()

    #: The size of the file.
    size = fields.Integer()

    #: The unique IDs of the Stories associated with this file.
    story_ids = fields.Nested(fields.Integer, many=True)

    #: The url where the thumbnail of the file can be found in Clubhouse.
    thumbnail_url = fields.String(allow_none=True)

    #: The time/date that the file was updated.
    updated_at = fields.Date(allow_none=True)

    #: The unique ID of the Member who uploaded the file.
    uploader_id = fields.UUID()

    #: The URL for the file.
    url = fields.String(allow_none=True)

class Icon(Schema):
    #: The time/date that the Icon was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique ID of the Icon.
    id = fields.UUID()

    #: The time/date that the Icon was updated.
    updated_at = fields.Date()

    #: The URL of the Icon.
    url = fields.String()

class LabelStats(Schema):
    #: The total number of Epics with this Label.
    num_epics = fields.Integer()

    #: The total number of completed points with this Label.
    num_points_completed = fields.Integer()

    #: The total number of in-progress points with this Label.
    num_points_in_progress = fields.Integer()

    #: The total number of points with this Label.
    num_points_total = fields.Integer()

    #: The total number of completed Stories with this Label.
    num_stories_completed = fields.Integer()

    #: The total number of in-progress Stories with this Label.
    num_stories_in_progress = fields.Integer()

    #: The total number of Stories with this Label.
    num_stories_total = fields.Integer()

    #: The total number of Stories with no point estimate with this Label.
    num_stories_unestimated = fields.Integer()

class LinkedFile(Schema):
    #: The content type of the image (e.g. txt/plain).
    content_type = fields.String(allow_none=True)

    #: The time/date the LinkedFile was created.
    created_at = fields.Date()

    #: The description of the file.
    description = fields.String(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique identified of the file.
    id = fields.Integer()

    #: The members that are mentioned in the description of the file.
    mention_ids = fields.Nested(fields.UUID, many=True)

    #: The name of the linked file.
    name = fields.String()

    #: The filesize, if the integration provided it.
    size = fields.Integer(allow_none=True)

    #: The IDs of the stories this file is attached to.
    story_ids = fields.Nested(fields.Integer, many=True)

    #: The URL of the file thumbnail, if the integration provided it.
    thumbnail_url = fields.String(allow_none=True)

    #: The integration type (e.g. google, dropbox, box).
    type = fields.String()

    #: The time/date the LinkedFile was updated.
    updated_at = fields.Date()

    #: The UUID of the member that uploaded the file.
    uploader_id = fields.UUID()

    #: The URL of the file.
    url = fields.String()

class ProjectStats(Schema):
    #: The total number of points in this Project.
    num_points = fields.Integer()

    #: The total number of stories in this Project.
    num_stories = fields.Integer()

class Repository(Schema):
    #: The time/date the Repository was created.
    created_at = fields.Date(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: The GitHub unique identifier for the Repository.
    external_id = fields.String(allow_none=True)

    #: The full name of the GitHub repository.
    full_name = fields.String(allow_none=True)

    #: The ID associated to the GitHub repository in Clubhouse.
    id = fields.Integer(allow_none=True)

    #: The shorthand name of the GitHub repository.
    name = fields.String(allow_none=True)

    #: The type of Repository. Currently this can only be github.
    type = fields.String()

    #: The time/date the Repository was updated.
    updated_at = fields.Date(allow_none=True)

    #: The URL of the Repository.
    url = fields.String(allow_none=True)

class TypedStoryLink(Schema):
    #: The time/date when the Story link was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique identifier of the Story Link.
    id = fields.Integer()

    #: The ID of the object Story.
    object_id = fields.Integer()

    #: The ID of the subject Story.
    subject_id = fields.Integer()

    #: This indicates whether the Story is the subject or object in the Story
    #: Link.
    type = fields.String()

    #: The time/date when the Story link was updated.
    updated_at = fields.Date()

    #: How the subject Story acts on the object Story.  This can be blocks,
    #: duplicates, or relates to.
    verb = fields.String()

class Task(Schema):
    #: True/false boolean indicating whether the Task has been completed.
    complete = fields.Boolean()

    #: The time/date the Task was completed.
    completed_at = fields.Date(allow_none=True)

    #: The time/date the Task was created.
    created_at = fields.Date()

    #: Full text of the Task.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Task has
    #: been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: The unique ID of the Task.
    id = fields.Integer()

    #: An array of UUIDs of Members mentioned in this Task.
    mention_ids = fields.Nested(fields.UUID, many=True)

    #: An array of UUIDs of the Owners of this Task.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: The number corresponding to the Tasks position within a list of Tasks on
    #: a Story.
    position = fields.Integer()

    #: The unique identifier of the parent Story.
    story_id = fields.Integer()

    #: The time/date the Task was updated.
    updated_at = fields.Date(allow_none=True)

class StoryLink(Schema):
    #: The time/date when the Story link was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique identifier of the Story Link.
    id = fields.Integer()

    #: The ID of the object Story.
    object_id = fields.Integer()

    #: The ID of the Subject story.
    subject_id = fields.Integer()

    #: The time/date when the Story Link was last updated.
    updated_at = fields.Date()

    #: The type of Story Link. This can be blocks, duplicates, or relates to.
    verb = fields.String()

class WorkflowState(Schema):
    #: The hex color for this Workflow State.
    color = fields.String()

    #: The time/date the Workflow State was created.
    created_at = fields.Date()

    #: The description of what sort of Stories belong in that Workflow state.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique ID of the Workflow State.
    id = fields.Integer()

    #: The Workflow States name.
    name = fields.String()

    #: The number of Stories currently in that Workflow State.
    num_stories = fields.Integer()

    #: The position that the Workflow State is in, starting with 0 at the left.
    position = fields.Integer()

    #: The type of Workflow State (Unstarted, Started, or Finished)
    type = fields.String()

    #: When the Workflow State was last updated.
    updated_at = fields.Date()

    #: The verb that triggers a move to that Workflow State when making GitHub
    #: commits.
    verb = fields.String(allow_none=True)

class Branch(Schema):
    #: The time/date the Branch was created.
    created_at = fields.Date(allow_none=True)

    #: A true/false boolean indicating if the Branch has been deleted.
    deleted = fields.Boolean()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique identifier of the Branch.
    id = fields.Integer(allow_none=True)

    #: The IDs of the Branches the Branch has been merged into.
    merged_branch_ids = fields.Nested(fields.Integer, many=True)

    #: The name of the Branch.
    name = fields.String()

    #: A true/false boolean indicating if the Branch is persistent; e.g. master.
    persistent = fields.Boolean()

    #: An array of PullRequests attached to the Branch (there is usually only
    #: one).
    pull_requests = fields.Nested(PullRequest, many=False)

    #: The ID of the Repository that contains the Branch.
    repository_id = fields.Integer(allow_none=True)

    #: The time/date the Branch was updated.
    updated_at = fields.Date(allow_none=True)

    #: The URL of the Branch.
    url = fields.String()

class Milestone(Schema):
    #: An array of Categories attached to the Milestone.
    categories = fields.Nested(Category, many=False)

    #: A true/false boolean indicating if the Milestone has been completed.
    completed = fields.Boolean()

    #: The time/date the Milestone was completed.
    completed_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Milestone was completed.
    completed_at_override = fields.Date(allow_none=True)

    #: The time/date the Milestone was created.
    created_at = fields.Date()

    #: The Milestones description.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique ID of the Milestone.
    id = fields.Integer()

    #: The name of the Milestone.
    name = fields.String()

    #: A number representing the position of the Milestone in relation to every
    #: other Milestone within the Organization.
    position = fields.Integer()

    #: A true/false boolean indicating if the Milestone has been started.
    started = fields.Boolean()

    #: The time/date the Milestone was started.
    started_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Milestone was started.
    started_at_override = fields.Date(allow_none=True)

    #: The workflow state that the Milestone is in.
    state = fields.String()

    #: The time/date the Milestone was updated.
    updated_at = fields.Date()

class Commit(Schema):
    #: The email address of the GitHub user that authored the Commit.
    author_email = fields.String()

    #: The ID of the Member that authored the Commit, if known.
    author_id = fields.UUID(allow_none=True)

    #: The Identity of the GitHub user that authored the Commit.
    author_identity = fields.Nested(Identity, many=False)

    #: The time/date the Commit was created.
    created_at = fields.Date()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The Commit hash.
    hash = fields.String()

    #: The unique identifier of the Commit.
    id = fields.Integer(allow_none=True)

    #: The IDs of the Branches the Commit has been merged into.
    merged_branch_ids = fields.Nested(fields.Integer, many=True)

    #: The Commit message.
    message = fields.String()

    #: The ID of the Repository that contains the Commit.
    repository_id = fields.Integer(allow_none=True)

    #: The time/date the Commit was pushed.
    timestamp = fields.Date()

    #: The time/date the Commit was updated.
    updated_at = fields.Date(allow_none=True)

    #: The URL of the Commit.
    url = fields.String()

class CreateStoryParams(Schema):
    #: An array of comments to add to the story.
    comments = fields.Nested(CreateCommentParams, many=False)

    #: A manual override for the time/date the Story was completed.
    completed_at_override = fields.Date()

    #: The time/date the Story was created.
    created_at = fields.Date()

    #: The due date of the story.
    deadline = fields.Date(allow_none=True)

    #: The description of the story.
    description = fields.String()

    #: The ID of the epic the story belongs to.
    epic_id = fields.Integer(allow_none=True)

    #: The numeric point estimate of the story. Can also be null, which means
    #: unestimated.
    estimate = fields.Integer(allow_none=True)

    #: An optional user-defined ID perhaps associating Task with an outside
    #: tool.
    external_id = fields.String()

    #: An array of IDs of files attached to the story.
    file_ids = fields.Nested(fields.Integer, many=True)

    #: An array of UUIDs of the followers of this story.
    follower_ids = fields.Nested(fields.UUID, many=True)

    #: An array of labels attached to the story.
    labels = fields.Nested(CreateLabelParams, many=False)

    #: An array of IDs of linked files attached to the story.
    linked_file_ids = fields.Nested(fields.Integer, many=True)

    #: The name of the story.
    name = fields.String()

    #: An array of UUIDs of the owners of this story.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: The ID of the project the story belongs to.
    project_id = fields.Integer()

    #: The ID of the member that requested the story.
    requested_by_id = fields.UUID()

    #: A manual override for the time/date the Story was started.
    started_at_override = fields.Date()

    #: An array of story links attached to the story.
    story_links = fields.Nested(CreateStoryLinkParams, many=False)

    #: The type of story (feature, bug, chore).
    story_type = fields.String(validate=validate.OneOf("bug", "chore", "feature"))

    #: An array of tasks connected to the story.
    tasks = fields.Nested(CreateTaskParams, many=False)

    #: The time/date the Story was updated.
    updated_at = fields.Date()

    #: The ID of the workflow state the story is currently in.
    workflow_state_id = fields.Integer()

class Profile(Schema):
    #: A true/false boolean indicating whether the Member has been deactivated
    #: within Clubhouse.
    deactivated = fields.Boolean()

    #: The Members avatar Icon.
    display_icon = fields.Nested(Icon, many=False)

    #: The primary email address of the Member with the Organization.
    email_address = fields.String(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: This is the gravatar hash associated with email_address.
    gravatar_hash = fields.String(allow_none=True)

    #: The unique identifier of the profile.
    id = fields.UUID()

    #: The Members username within the Organization.
    mention_name = fields.String()

    #: The Members name within the Organization.
    name = fields.String()

    #: If Two Factor Authentication is activated for this User.
    two_factor_auth_activated = fields.Boolean()

class Label(Schema):
    #: A true/false boolean indicating if the Label has been archived.
    archived = fields.Boolean()

    #: The hex color to be displayed with the Label (for example, #ff0000).
    color = fields.String(allow_none=True)

    #: The time/date that the Label was created.
    created_at = fields.Date(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Label
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: The unique ID of the Label.
    id = fields.Integer()

    #: The name of the Label.
    name = fields.String()

    #: A group of calculated values for this Label.
    stats = fields.Nested(LabelStats, many=False)

    #: The time/date that the Label was updated.
    updated_at = fields.Date(allow_none=True)

class Project(Schema):
    #: The Project abbreviation used in Story summaries. Should be kept to 3
    #: characters at most.
    abbreviation = fields.String(allow_none=True)

    #: True/false boolean indicating whether the Project is in an Archived
    #: state.
    archived = fields.Boolean()

    #: The color associated with the Project in the Clubhouse member interface.
    color = fields.String(allow_none=True)

    #: The time/date that the Project was created.
    created_at = fields.Date(allow_none=True)

    #: The number of days before the thermometer appears in the Story summary.
    days_to_thermometer = fields.Integer()

    #: The description of the Project.
    description = fields.String(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Project
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: An array of UUIDs for any Members listed as Followers.
    follower_ids = fields.Nested(fields.UUID, many=True)

    #: The unique ID of the Project.
    id = fields.Integer()

    #: The number of weeks per iteration in this Project.
    iteration_length = fields.Integer()

    #: The name of the Project
    name = fields.String()

    #: Configuration to enable or disable thermometers in the Story summary.
    show_thermometer = fields.Boolean()

    #: The date at which the Project was started.
    start_time = fields.Date()

    #: A group of calculated values for this Project.
    stats = fields.Nested(ProjectStats, many=False)

    #: The ID of the team the project belongs to.
    team_id = fields.Integer()

    #: The time/date that the Project was last updated.
    updated_at = fields.Date(allow_none=True)

class Workflow(Schema):
    #: The date the Workflow was created.
    created_at = fields.Date()

    #: The unique ID of the default state that new Stories are entered into.
    default_state_id = fields.Integer()

    #: A description of the workflow.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique ID of the Workflow.
    id = fields.Integer()

    #: The name of the workflow.
    name = fields.String()

    #: A map of the states in this Workflow.
    states = fields.Nested(WorkflowState, many=False)

    #: The ID of the team the workflow belongs to.
    team_id = fields.Integer()

    #: The date the Workflow was updated.
    updated_at = fields.Date()

class Member(Schema):
    #: The time/date the Member was created.
    created_at = fields.Date(allow_none=True)

    #: True/false boolean indicating whether the Member has been disabled within
    #: this Organization.
    disabled = fields.Boolean()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The Members ID in Clubhouse.
    id = fields.UUID()

    #: A group of Member profile details.
    profile = fields.Nested(Profile, many=False)

    #: The Members role in the Clubhouse organization.
    role = fields.String()

    #: The time/date the Member was last updated.
    updated_at = fields.Date(allow_none=True)

class Story(Schema):
    #: The clubhouse application url for the story.
    app_url = fields.String()

    #: True if the story has been archived or not.
    archived = fields.Boolean()

    #: A true/false boolean indicating if the Story is currently blocked.
    blocked = fields.Boolean()

    #: A true/false boolean indicating if the Story is currently a blocker of
    #: another story.
    blocker = fields.Boolean()

    #: An array of Git branches attached to the story.
    branches = fields.Nested(Branch, many=False)

    #: An array of comments attached to the story.
    comments = fields.Nested(Comment, many=False)

    #: An array of commits attached to the story.
    commits = fields.Nested(Commit, many=False)

    #: A true/false boolean indicating if the Story has been completed.
    completed = fields.Boolean()

    #: The time/date the Story was completed.
    completed_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Story was completed.
    completed_at_override = fields.Date(allow_none=True)

    #: The time/date the Story was created.
    created_at = fields.Date()

    #: The due date of the story.
    deadline = fields.Date(allow_none=True)

    #: The description of the story.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The ID of the epic the story belongs to.
    epic_id = fields.Integer(allow_none=True)

    #: The numeric point estimate of the story. Can also be null, which means
    #: unestimated.
    estimate = fields.Integer(allow_none=True)

    #: This field can be set to another unique ID. In the case that the Story
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: An array of files attached to the story.
    files = fields.Nested(File, many=False)

    #: An array of UUIDs of the followers of this story.
    follower_ids = fields.Nested(fields.UUID, many=True)

    #: The unique identifier of the story.
    id = fields.Integer()

    #: An array of labels attached to the story.
    labels = fields.Nested(Label, many=False)

    #: An array of linked files attached to the story.
    linked_files = fields.Nested(LinkedFile, many=False)

    #: The time/date the Story was last changed workflow-state.
    moved_at = fields.Date(allow_none=True)

    #: The name of the story.
    name = fields.String()

    #: An array of UUIDs of the owners of this story.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: A number representing the position of the story in relation to every
    #: other story in the current project.
    position = fields.Integer()

    #: The ID of the project the story belongs to.
    project_id = fields.Integer()

    #: The ID of the Member that requested the story.
    requested_by_id = fields.UUID()

    #: A true/false boolean indicating if the Story has been started.
    started = fields.Boolean()

    #: The time/date the Story was started.
    started_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Story was started.
    started_at_override = fields.Date(allow_none=True)

    #: An array of story links attached to the story.
    story_links = fields.Nested(TypedStoryLink, many=False)

    #: The type of story (feature, bug, chore).
    story_type = fields.String()

    #: An array of tasks connected to the story.
    tasks = fields.Nested(Task, many=False)

    #: The time/date the Story was updated.
    updated_at = fields.Date(allow_none=True)

    #: The ID of the workflow state the story is currently in.
    workflow_state_id = fields.Integer()

class StorySlim(Schema):
    #: The clubhouse application url for the story.
    app_url = fields.String()

    #: True if the story has been archived or not.
    archived = fields.Boolean()

    #: A true/false boolean indicating if the Story is currently blocked.
    blocked = fields.Boolean()

    #: A true/false boolean indicating if the Story is currently a blocker of
    #: another story.
    blocker = fields.Boolean()

    #: An array of IDs of Comments attached to the story.
    comment_ids = fields.Nested(fields.Integer, many=True)

    #: A true/false boolean indicating if the Story has been completed.
    completed = fields.Boolean()

    #: The time/date the Story was completed.
    completed_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Story was completed.
    completed_at_override = fields.Date(allow_none=True)

    #: The time/date the Story was created.
    created_at = fields.Date()

    #: The due date of the story.
    deadline = fields.Date(allow_none=True)

    #: A string description of this resource.
    entity_type = fields.String()

    #: The ID of the epic the story belongs to.
    epic_id = fields.Integer(allow_none=True)

    #: The numeric point estimate of the story. Can also be null, which means
    #: unestimated.
    estimate = fields.Integer(allow_none=True)

    #: This field can be set to another unique ID. In the case that the Story
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: An array of IDs of Files attached to the story.
    file_ids = fields.Nested(fields.Integer, many=True)

    #: An array of UUIDs for any Members listed as Followers.
    follower_ids = fields.Nested(fields.UUID, many=True)

    #: The unique identifier of the story.
    id = fields.Integer()

    #: An array of labels attached to the story.
    labels = fields.Nested(Label, many=False)

    #: An array of IDs of LinkedFiles attached to the story.
    linked_file_ids = fields.Nested(fields.Integer, many=True)

    #: The time/date the Story was last changed workflow-state.
    moved_at = fields.Date(allow_none=True)

    #: The name of the story.
    name = fields.String()

    #: An array of UUIDs of the owners of this story.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: A number representing the position of the story in relation to every
    #: other story in the current project.
    position = fields.Integer()

    #: The ID of the project the story belongs to.
    project_id = fields.Integer()

    #: The ID of the Member that requested the story.
    requested_by_id = fields.UUID()

    #: A true/false boolean indicating if the Story has been started.
    started = fields.Boolean()

    #: The time/date the Story was started.
    started_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Story was started.
    started_at_override = fields.Date(allow_none=True)

    #: An array of story links attached to the story.
    story_links = fields.Nested(TypedStoryLink, many=False)

    #: The type of story (feature, bug, chore).
    story_type = fields.String()

    #: An array of IDs of Tasks attached to the story.
    task_ids = fields.Nested(fields.Integer, many=True)

    #: The time/date the Story was updated.
    updated_at = fields.Date(allow_none=True)

    #: The ID of the workflow state the story is currently in.
    workflow_state_id = fields.Integer()

class StorySearch(Schema):
    #: The clubhouse application url for the story.
    app_url = fields.String()

    #: True if the story has been archived or not.
    archived = fields.Boolean()

    #: A true/false boolean indicating if the Story is currently blocked.
    blocked = fields.Boolean()

    #: A true/false boolean indicating if the Story is currently a blocker of
    #: another story.
    blocker = fields.Boolean()

    #: A true/false boolean indicating if the Story has been completed.
    completed = fields.Boolean()

    #: The time/date the Story was completed.
    completed_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Story was completed.
    completed_at_override = fields.Date(allow_none=True)

    #: The time/date the Story was created.
    created_at = fields.Date()

    #: The due date of the story.
    deadline = fields.Date(allow_none=True)

    #: The description of the story.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The ID of the epic the story belongs to.
    epic_id = fields.Integer(allow_none=True)

    #: The numeric point estimate of the story. Can also be null, which means
    #: unestimated.
    estimate = fields.Integer(allow_none=True)

    #: This field can be set to another unique ID. In the case that the Story
    #: has been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: An array of UUIDs of the followers of this story.
    follower_ids = fields.Nested(fields.UUID, many=True)

    #: The unique identifier of the story.
    id = fields.Integer()

    #: An array of labels attached to the story.
    labels = fields.Nested(Label, many=False)

    #: The time/date the Story was last changed workflow-state.
    moved_at = fields.Date(allow_none=True)

    #: The name of the story.
    name = fields.String()

    #: An array of UUIDs of the owners of this story.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: A number representing the position of the story in relation to every
    #: other story in the current project.
    position = fields.Integer()

    #: The ID of the project the story belongs to.
    project_id = fields.Integer()

    #: The ID of the Member that requested the story.
    requested_by_id = fields.UUID()

    #: A true/false boolean indicating if the Story has been started.
    started = fields.Boolean()

    #: The time/date the Story was started.
    started_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Story was started.
    started_at_override = fields.Date(allow_none=True)

    #: An array of story links attached to the story.
    story_links = fields.Nested(TypedStoryLink, many=False)

    #: The type of story (feature, bug, chore).
    story_type = fields.String()

    #: The time/date the Story was updated.
    updated_at = fields.Date(allow_none=True)

    #: The ID of the workflow state the story is currently in.
    workflow_state_id = fields.Integer()

class Epic(Schema):
    #: True/false boolean that indicates whether the Epic is archived or not.
    archived = fields.Boolean()

    #: A nested array of threaded comments.
    comments = fields.Nested(ThreadedComment, many=False)

    #: A true/false boolean indicating if the Epic has been completed.
    completed = fields.Boolean()

    #: The time/date the Epic was completed.
    completed_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Epic was completed.
    completed_at_override = fields.Date(allow_none=True)

    #: The time/date the Epic was created.
    created_at = fields.Date(allow_none=True)

    #: The Epics deadline.
    deadline = fields.Date(allow_none=True)

    #: The Epics description.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: This field can be set to another unique ID. In the case that the Epic has
    #: been imported from another tool, the ID in the other tool can be
    #: indicated here.
    external_id = fields.String(allow_none=True)

    #: An array of UUIDs for any Members you want to add as Followers on this
    #: Epic.
    follower_ids = fields.Nested(fields.UUID, many=True)

    #: The unique ID of the Epic.
    id = fields.Integer()

    #: An array of Labels attached to the Epic.
    labels = fields.Nested(Label, many=False)

    #: The ID of the Milestone this Epic is related to.
    milestone_id = fields.Integer(allow_none=True)

    #: The name of the Epic.
    name = fields.String()

    #: An array of UUIDs for any members you want to add as Owners on this new
    #: Epic.
    owner_ids = fields.Nested(fields.UUID, many=True)

    #: The Epics relative position in the Epic workflow state.
    position = fields.Integer()

    #: The IDs of Projects related to this Epic.
    project_ids = fields.Nested(fields.Integer, many=True)

    #: The ID of the member that requested the epic.
    requested_by_id = fields.UUID()

    #: A true/false boolean indicating if the Epic has been started.
    started = fields.Boolean()

    #: The time/date the Epic was started.
    started_at = fields.Date(allow_none=True)

    #: A manual override for the time/date the Epic was started.
    started_at_override = fields.Date(allow_none=True)

    #: The workflow state that the Epic is in.
    state = fields.String()

    #: A group of calculated values for this Epic.
    stats = fields.Nested(EpicStats, many=False)

    #: The time/date the Epic was updated.
    updated_at = fields.Date(allow_none=True)

class Team(Schema):
    #: The time/date the Team was created.
    created_at = fields.Date()

    #: The description of the Team.
    description = fields.String()

    #: A string description of this resource.
    entity_type = fields.String()

    #: The unique identifier of the Team.
    id = fields.Integer()

    #: The name of the Team.
    name = fields.String()

    #: A number representing the position of the Team in relation to every other
    #: Team within the Organization.
    position = fields.Integer()

    #: An array of IDs of projects within the Team.
    project_ids = fields.Nested(fields.Integer, many=True)

    #: The time/date the Team was last updated.
    updated_at = fields.Date()

    #: Details of the workflow associated with the Team.
    workflow = fields.Nested(Workflow, many=False)

class SearchResults(Schema):
    #: A list of search results.
    data = fields.Nested(StorySearch, many=False)

    #: The next page token.
    next = fields.String()

    #: The total number of matches for the search query.
    total = fields.Integer()
