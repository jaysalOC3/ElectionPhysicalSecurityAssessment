# CommentCreateView
- Description: Creates a new comment for an assessment or a specific question.
- URL: `/comments/create/`
- HTTP Method: POST
- Request Parameters:
  - `assessment_id`: The ID of the assessment associated with the comment.
  - `question_id`: (Optional) The ID of the specific question associated with the comment.
  - `content`: The content of the comment.
- Response:
  - HTTP Status Code: 201 (Created)
  - Content: The created comment in JSON format.

# CommentListView
- Description: Retrieves a list of comments for an assessment or a specific question.
- URL: `/comments/`
- HTTP Method: GET
- Request Parameters:
  - `assessment_id`: The ID of the assessment to retrieve comments for.
  - `question_id`: (Optional) The ID of the specific question to retrieve comments for.
- Response:
  - HTTP Status Code: 200 (OK)
  - Content: List of comments in JSON format.

# UserProfileView
- Description: Displays the user's profile information.
- URL: `/profile/`
- HTTP Method: GET
- Request Parameters: None
- Response:
  - HTTP Status Code: 200 (OK)
  - Content: Rendered HTML template with the user's profile information.

# UserUpdateView
- Description: Allows users to update their profile information.
- URL: `/profile/update/`
- HTTP Method: GET, POST
- Request Parameters: None
- Response:
  - GET:
    - HTTP Status Code: 200 (OK)
    - Content: Rendered HTML template with a form to update the user's profile information.
  - POST:
    - HTTP Status Code: 302 (Found)
    - Redirect: `/profile/`

# UserAssessmentListView
- Description: Shows a list of assessments the user is associated with.
- URL: `/profile/assessments/`
- HTTP Method: GET
- Request Parameters: None
- Response:
  - HTTP Status Code: 200 (OK)
  - Content: Rendered HTML template with a list of assessments the user is associated with.

# UserInvitationListView
- Description: Displays the list of assessment invitations received by the user.
- URL: `/profile/invitations/`
- HTTP Method: GET
- Request Parameters: None
- Response:
  - HTTP Status Code: 200 (OK)
  - Content: Rendered HTML template with a list of assessment invitations received by the user.

# AcceptInvitationView
- Description: Allows users to accept an assessment invitation.
- URL: `/invitations/<invitation_id>/accept/`
- HTTP Method: POST
- Request Parameters:
  - `invitation_id`: The ID of the invitation to accept.
- Response:
  - HTTP Status Code: 302 (Found)
  - Redirect: `/profile/assessments/`

# DeclineInvitationView
- Description: Allows users to decline an assessment invitation.
- URL: `/invitations/<invitation_id>/decline/`
- HTTP Method: POST
- Request Parameters:
  - `invitation_id`: The ID of the invitation to decline.
- Response:
  - HTTP Status Code: 302 (Found)
  - Redirect: `/profile/invitations/`