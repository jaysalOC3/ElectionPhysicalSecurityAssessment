# User model represents the users of the system
## User
### Fields
- **username**
  - Type: CharField
  - Max Length: 150
  - Unique: true
  - Description: Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only.
- **email**
  - Type: EmailField
  - Unique: true
  - Description: Required. A valid email address.
- **password**
  - Type: CharField
  - Max Length: 128
  - Description: Required. The hashed password.
- **first_name**
  - Type: CharField
  - Max Length: 30
  - Blank: true
  - Description: Optional. 30 characters or fewer.
- **last_name**
  - Type: CharField
  - Max Length: 150
  - Blank: true
  - Description: Optional. 150 characters or fewer.
- **is_active**
  - Type: BooleanField
  - Default: true
  - Description: Designates whether this user should be treated as active.
- **is_staff**
  - Type: BooleanField
  - Default: false
  - Description: Designates whether the user can log into the admin site.
- **is_superuser**
  - Type: BooleanField
  - Default: false
  - Description: Designates that this user has all permissions without explicitly assigning them.
- **date_joined**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The date and time when the user account was created.
- **last_login**
  - Type: DateTimeField
  - Null: true
  - Blank: true
  - Description: The last date and time when the user logged in.
- **assessments**
  - Type: ManyToManyField
  - Related Model: Assessment
  - Through: UserAssessment
  - Description: The assessments the user is associated with.
- **auto_accept_invites**
  - Type: BooleanField
  - Default: false
  - Description: Indicates whether the user automatically accepts assessment invitations.
- **role**
  - Type: ForeignKey
  - Related Model: UserRole
  - On Delete: CASCADE
  - Description: The role assigned to the user.

### Methods
- **__str__**
  - Description: Returns the username as the string representation of the user.
- **get_full_name**
  - Description: Returns the first_name plus the last_name, with a space in between.
- **get_short_name**
  - Description: Returns the short name for the user (typically the first name).

# UserRole model represents the roles assigned to users
## UserRole
### Fields
- **name**
  - Type: CharField
  - Max Length: 50
  - Unique: true
  - Description: The name of the role (e.g., Site Leader, Assessor, Reviewer, Admin).
- **permissions**
  - Type: JSONField
  - Description: The permissions associated with the role, stored as a JSON object.

# Comment model represents comments or discussions related to an assessment or a specific question
## Comment
### Fields
- **assessment**
  - Type: ForeignKey
  - Related Model: Assessment
  - On Delete: CASCADE
  - Description: The assessment associated with the comment.
- **question**
  - Type: ForeignKey
  - Related Model: AssessmentQuestion
  - Null: true
  - Blank: true
  - On Delete: CASCADE
  - Description: The specific question associated with the comment.
- **user**
  - Type: ForeignKey
  - Related Model: User
  - On Delete: CASCADE
  - Description: The user who made the comment.
- **content**
  - Type: TextField
  - Description: The content of the comment.
- **created_at**
  - Type: DateTimeField
  - Auto Now Add: true
  - Description: The timestamp of when the comment was created.