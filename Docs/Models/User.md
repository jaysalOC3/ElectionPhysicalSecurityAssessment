# User model represents the users of the system
User:
  fields:
    username:
      type: CharField
      max_length: 150
      unique: true
      description: "Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only."
    
    email:
      type: EmailField
      unique: true
      description: "Required. A valid email address."
    
    password:
      type: CharField
      max_length: 128
      description: "Required. The hashed password."
    
    first_name:
      type: CharField
      max_length: 30
      blank: true
      description: "Optional. 30 characters or fewer."
    
    last_name:
      type: CharField
      max_length: 150
      blank: true
      description: "Optional. 150 characters or fewer."
    
    is_active:
      type: BooleanField
      default: true
      description: "Designates whether this user should be treated as active."
    
    is_staff:
      type: BooleanField
      default: false
      description: "Designates whether the user can log into the admin site."
    
    is_superuser:
      type: BooleanField
      default: false
      description: "Designates that this user has all permissions without explicitly assigning them."
    
    date_joined:
      type: DateTimeField
      auto_now_add: true
      description: "The date and time when the user account was created."
    
    last_login:
      type: DateTimeField
      null: true
      blank: true
      description: "The last date and time when the user logged in."
    
    assessments:
      type: ManyToManyField
      related_model: Assessment
      through: UserAssessment
      description: "The assessments the user is associated with."
    
    auto_accept_invites:
      type: BooleanField
      default: false
      description: "Indicates whether the user automatically accepts assessment invitations."

  methods:
    __str__:
      description: "Returns the username as the string representation of the user."
    
    get_full_name:
      description: "Returns the first_name plus the last_name, with a space in between."
    
    get_short_name:
      description: "Returns the short name for the user (typically the first name)."
    