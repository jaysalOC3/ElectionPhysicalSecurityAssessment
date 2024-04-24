# UserRegistrationForm for user registration
## UserRegistrationForm
### Fields
- **username**
  - Type: CharField
  - Widget: TextInput
  - Description: The username of the user.
- **email**
  - Type: EmailField
  - Widget: EmailInput
  - Description: The email address of the user.
- **password1**
  - Type: CharField
  - Widget: PasswordInput
  - Description: The password of the user.
- **password2**
  - Type: CharField
  - Widget: PasswordInput
  - Description: The password confirmation.
- **first_name**
  - Type: CharField
  - Widget: TextInput
  - Required: false
  - Description: The first name of the user.
- **last_name**
  - Type: CharField
  - Widget: TextInput
  - Required: false
  - Description: The last name of the user.
- **auto_accept_invites**
  - Type: BooleanField
  - Description: Indicates whether the user automatically accepts assessment invitations.
- **role**
  - Type: ModelChoiceField
  - Queryset: UserRole.objects.all()
  - Description: The role assigned to the user.

# UserUpdateForm for updating user profile
## UserUpdateForm
### Fields
- **first_name**
  - Type: CharField
  - Widget: TextInput
  - Required: false
  - Description: The first name of the user.
- **last_name**
  - Type: CharField
  - Widget: TextInput
  - Required: false
  - Description: The last name of the user.
- **email**
  - Type: EmailField
  - Widget: EmailInput
  - Description: The email address of the user.
- **auto_accept_invites**
  - Type: BooleanField
  - Description: Indicates whether the user automatically accepts assessment invitations.
- **role**
  - Type: ModelChoiceField
  - Queryset: UserRole.objects.all()
  - Description: The role assigned to the user.

# CommentForm for creating comments
## CommentForm
### Fields
- **content**
  - Type: CharField
  - Widget: Textarea
  - Description: The content of the comment.

NotificationPreferenceForm for updating notification preferences
NotificationPreferenceForm
Fields

email_enabled

Type: BooleanField
Description: Indicates whether email notifications are enabled for the user.


sms_enabled

Type: BooleanField
Description: Indicates whether SMS notifications are enabled for the user.


notification_types

Type: MultipleChoiceField
Choices:

"assessment_invitation"
"assessment_approval"
"assessment_deadline"


Description: The types of notifications the user wants to receive.