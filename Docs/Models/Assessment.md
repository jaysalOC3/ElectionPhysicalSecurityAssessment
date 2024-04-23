# Assessment model represents the assessments in the system
Assessment:
  fields:
    name:
      type: CharField
      max_length: 255
      description: "The name of the assessment."
    
    description:
      type: TextField
      blank: true
      description: "A description of the assessment."
    
    start_date:
      type: DateTimeField
      description: "The start date and time of the assessment."
    
    end_date:
      type: DateTimeField
      description: "The end date and time of the assessment."
    
    participants:
      type: ManyToManyField
      related_model: User
      through: UserAssessment
      description: "The users participating in the assessment."

    polling_site:
      type: ForeignKey
      related_model: PollingSite
      null: true
      blank: true
      on_delete: SET_NULL
      description: "The polling site assigned to the assessment."

    methods:
      calculate_overall_score:
        description: "Calculates the overall maturity score for the assessment based on the individual question responses."
        return_type: float

# UserAssessment model represents the relationship between users and assessments
UserAssessment:
  fields:
    user:
      type: ForeignKey
      related_model: User
      on_delete: CASCADE
      description: "The user associated with the assessment."
    
    assessment:
      type: ForeignKey
      related_model: Assessment
      on_delete: CASCADE
      description: "The assessment the user is associated with."
    
    joined_at:
      type: DateTimeField
      auto_now_add: true
      description: "The date and time when the user joined the assessment."
    
    invited_by:
      type: ForeignKey
      related_model: User
      null: true
      blank: true
      on_delete: SET_NULL
      description: "The user who invited this user to the assessment (if applicable)."
    
    status:
      type: CharField
      max_length: 20
      choices:
        - "invited"
        - "joined"
        - "completed"
      default: "invited"
      description: "The status of the user's participation in the assessment."

# AssessmentQuestion model represents a question in an assessment
AssessmentQuestion:
  fields:
    question_text:
      type: TextField
      description: "The text of the question."
    
    question_type:
      type: CharField
      max_length: 20
      choices:
        - "yes_no"
        - "multiple_choice"
        - "text"
      default: "yes_no"
      description: "The type of the question (yes/no, multiple choice, text)."
    
    choices:
      type: JSONField
      null: true
      blank: true
      description: "The choices for a multiple-choice question, stored as a JSON array."
    
    order:
      type: PositiveIntegerField
      default: 0
      description: "The order of the question within the assessment."
    
    created_at:
      type: DateTimeField
      auto_now_add: true
      description: "The timestamp of when the question was created."
    
    updated_at:
      type: DateTimeField
      auto_now: true
      description: "The timestamp of when the question was last updated."

  methods:
    __str__:
      description: "Returns the question text as the string representation of the question."

# AssessmentResponse model represents a single response to a question in an assessment
AssessmentResponse:
  fields:
    assessment:
      type: ForeignKey
      related_model: Assessment
      on_delete: CASCADE
      description: "The assessment to which the response belongs."
    
    question:
      type: ForeignKey
      related_model: AssessmentQuestion
      on_delete: CASCADE
      description: "The question to which the response belongs."
    
    maturity_score:
      type: IntegerField
      choices:
        - 0: "Not Implemented"
        - 1: "Partially Implemented"
        - 2: "Fully Implemented"
      description: "The maturity score for the response (0: Not Implemented, 1: Partially Implemented, 2: Fully Implemented)."
    
    notes:
      type: TextField
      blank: true
      description: "Additional notes or comments related to the response."
    
    user:
      type: ForeignKey
      related_model: User
      on_delete: CASCADE
      description: "The user who provided the response."
    
    timestamp:
      type: DateTimeField
      auto_now_add: true
      description: "The timestamp of when the response was submitted."
  
  methods:
    __str__:
      description: "Returns a string representation of the assessment response."
      return_type: str