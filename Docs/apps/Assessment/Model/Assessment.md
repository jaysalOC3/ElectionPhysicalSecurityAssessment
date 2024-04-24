# Assessment model represents the assessments in the system
## Assessment
### Fields
- **name**
  - Type: CharField
  - Max Length: 255
  - Description: The name of the assessment.
- **description**
  - Type: TextField
  - Blank: true
  - Description: A description of the assessment.
- **start_date**
  - Type: DateTimeField
  - Description: The start date and time of the assessment.
- **end_date**
  - Type: DateTimeField
  - Description: The end date and time of the assessment.
- **participants**
  - Type: ManyToManyField
  - Related Model: User
  - Through: UserAssessment
  - Description: The users participating in the assessment.
- **polling_site**
  - Type: ForeignKey
  - Related Model: PollingSite
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The polling site assigned to the assessment.
- **status**
  - Type: CharField
  - Max Length: 20
  - Choices:
    - "draft"
    - "in_progress"
    - "submitted"
    - "approved"
  - Default: "draft"
  - Description: The status of the assessment.
- **submitted_by**
  - Type: ForeignKey
  - Related Model: User
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The user who submitted the assessment.
- **submitted_at**
  - Type: DateTimeField
  - Null: true
  - Blank: true
  - Description: The timestamp of when the assessment was submitted.
- **approved_by**
  - Type: ForeignKey
  - Related Model: User
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The user who approved the assessment.
- **approved_at**
  - Type: DateTimeField
  - Null: true
  - Blank: true
  - Description: The timestamp of when the assessment was approved.

### Methods
- **calculate_overall_score**
  - Description: Calculates the overall maturity score for the assessment based on the individual question responses.
  - Return Type: float

# UserAssessment model represents the relationship between users and assessments
## UserAssessment
### Fields
- **user**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user associated with the assessment.
- **assessment**
  - Type: ForeignKey
  - Related Model: Assessment
  - On Delete: CASCADE
  - Description: The assessment the user is associated with.
- **joined_at**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The date and time when the user joined the assessment.
- **invited_by**
  - Type: ForeignKey
  - Related Model: User
  - Null: true
  - Blank: true
  - On Delete: SET_NULL
  - Description: The user who invited this user to the assessment (if applicable).
- **status**
  - Type: CharField
  - Max Length: 20
  - Choices:
    - "invited"
    - "joined"
    - "completed"
  - Default: "invited"
  - Description: The status of the user's participation in the assessment.
- **permission**
  - Type: ForeignKey
  - Related Model: UserAssessmentPermission
  - On Delete: CASCADE
  - Description: The permission associated with the user's access to the assessment.
- **assigned_sections**
  - Type: ManyToManyField
  - Related Model: AssessmentSection
  - Blank: true
  - Description: The sections of the assessment assigned to the user.

# AssessmentQuestion model represents a question in an assessment
## AssessmentQuestion
### Fields
- **question_text**
  - Type: TextField
  - Description: The text of the question.
- **question_type**
  - Type: CharField
  - Max Length: 20
  - Choices:
    - "yes_no"
    - "multiple_choice"
    - "text"
  - Default: "yes_no"
  - Description: The type of the question (yes/no, multiple choice, text).
- **choices**
  - Type: JSONField
  - Null: true
  - Blank: true
  - Description: The choices for a multiple-choice question, stored as a JSON array.
- **order**
  - Type: PositiveIntegerField
  - Default: 0
  - Description: The order of the question within the assessment.
- **created_at**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The timestamp of when the question was created.
- **updated_at**
  - Type: DateTimeField
  - Auto Now: true
  - Description: The timestamp of when the question was last updated.
- **section**
  - Type: ForeignKey
  - Related Model: AssessmentSection
  - On Delete: CASCADE
  - Description: The section to which the question belongs.

### Methods
- **__str__**
  - Description: Returns the question text as the string representation of the question.

# AssessmentResponse model represents a single response to a question in an assessment
## AssessmentResponse
### Fields
- **assessment**
  - Type: ForeignKey
  - Related Model: Assessment
  - On Delete: CASCADE
  - Description: The assessment to which the response belongs.
- **question**
  - Type: ForeignKey
  - Related Model: AssessmentQuestion
  - On Delete: CASCADE
  - Description: The question to which the response belongs.
- **maturity_score**
  - Type: IntegerField
  - Choices:
    - 0: "Not Implemented"
    - 1: "Partially Implemented"
    - 2: "Fully Implemented"
  - Description: The maturity score for the response (0: Not Implemented, 1: Partially Implemented, 2: Fully Implemented).
- **notes**
  - Type: TextField
  - Blank: true
  - Description: Additional notes or comments related to the response.
- **user**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user who provided the response.
- **timestamp**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The timestamp of when the response was submitted.
- **attachments**
  - Type: ManyToManyField
  - Related Model: Attachment
  - Blank: true
  - Description: The attachments (photos, documents) associated with the response.

### Methods
- **__str__**
  - Description: Returns a string representation of the assessment response.
  - Return Type: str

# UserAssessmentPermission model represents the permissions a user has for an assessment
## UserAssessmentPermission
### Fields
- **user**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user associated with the permission.
- **assessment**
  - Type: ForeignKey
  - Related Model: Assessment
  - On Delete: CASCADE
  - Description: The assessment associated with the permission.
- **permission**
  - Type: CharField
  - Max Length: 20
  - Choices:
    - "read"
    - "write"
  - Description: The permission level assigned to the user for the assessment.

### Meta
- **unique_together**
  - Fields: ('user', 'assessment', 'permission')
  - Description: Ensures that the combination of user, assessment, and permission is unique.

# AssessmentSection model represents a section within an assessment
## AssessmentSection
### Fields
- **name**
  - Type: CharField
  - Max Length: 255
  - Description: The name of the section.
- **description**
  - Type: TextField
  - Blank: true
  - Description: A description of the section.
- **order**
  - Type: PositiveIntegerField
  - Default: 0
  - Description: The order of the section within the assessment.
- **assessment**
  - Type: ForeignKey
  - Related Model: Assessment
  - On Delete: CASCADE
  - Description: The assessment to which the section belongs.

# Attachment model represents an attachment (photo, document) associated with an assessment response
## Attachment
### Fields
- **file**
  - Type: FileField
  - Upload To: 'attachments/'
  - Description: The uploaded file attachment.
- **name**
  - Type: CharField
  - Max Length: 255
  - Description: The name of the attachment.
- **description**
  - Type: TextField
  - Blank: true
  - Description: A description of the attachment.
- **uploaded_by**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user who uploaded the attachment.
- **uploaded_at**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The timestamp of when the attachment was uploaded.

# Report model represents a generated report for an assessment
## Report
### Fields
- **assessment**
  - Type: ForeignKey
  - Related Model: Assessment
  - On Delete: CASCADE
  - Description: The assessment associated with the report.
- **generated_by**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user who generated the report.
- **generated_at**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The timestamp of when the report was generated.
- **report_file**
  - Type: FileField
  - Upload To: 'reports/'
  - Description: The generated report file.

# Notification model represents notifications sent to users
## Notification
### Fields
- **user**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user associated with the notification.
- **message**
  - Type: TextField
  - Description: The notification message.
- **created_at**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The timestamp of when the notification was created.
- **is_read**
  - Type: BooleanField
  - Default: false
  - Description: Indicates whether the notification has been read by the user.

AssessmentReport model represents the generated reports for assessments
AssessmentReport
Fields

assessment

Type: ForeignKey
Related Model: Assessment
On Delete: CASCADE
Description: The assessment associated with the report.


report_type

Type: CharField
Max Length: 50
Choices:

"summary"
"detailed"
"aggregated"


Description: The type of report (summary, detailed, aggregated).


report_data

Type: JSONField
Description: The report data stored as a JSON object.


generated_at

Type: DateTimeField
Auto Now Add: true
Description: The timestamp of when the report was generated.

AssessmentCollaboration model represents the collaboration features for an assessment
AssessmentCollaboration
Fields

assessment

Type: OneToOneField
Related Model: Assessment
On Delete: CASCADE
Description: The assessment associated with the collaboration.


chat_enabled

Type: BooleanField
Default: true
Description: Indicates whether the chat feature is enabled for the assessment.


commenting_enabled

Type: BooleanField
Default: true
Description: Indicates whether the commenting feature is enabled for the assessment.



AssessmentChatMessage model represents a chat message in an assessment collaboration
AssessmentChatMessage
Fields

collaboration

Type: ForeignKey
Related Model: AssessmentCollaboration
On Delete: CASCADE
Description: The collaboration associated with the chat message.


user

Type: ForeignKey
Related Model: User
On Delete: CASCADE
Description: The user who sent the chat message.


message

Type: TextField
Description: The content of the chat message.


timestamp

Type: DateTimeField
Auto Now Add: true
Description: The timestamp of when the chat message was sent.



AssessmentComment model represents a comment in an assessment collaboration
AssessmentComment
Fields

collaboration

Type: ForeignKey
Related Model: AssessmentCollaboration
On Delete: CASCADE
Description: The collaboration associated with the comment.


user

Type: ForeignKey
Related Model: User
On Delete: CASCADE
Description: The user who posted the comment.


content

Type: TextField
Description: The content of the comment.


timestamp

Type: DateTimeField
Auto Now Add: true
Description: The timestamp of when the comment was posted.


parent_comment

Type: ForeignKey
Related Model: self
Null: true
Blank: true
On Delete: CASCADE
Description: The parent comment, if the comment is a reply to another comment.


mentioned_users

Type: ManyToManyField
Related Model: User
Blank: true
Description: The users mentioned or tagged in the comment.