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