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

### Methods
- **__str__**
  - Description: Returns a string representation of the assessment response.
  - Return Type: str
