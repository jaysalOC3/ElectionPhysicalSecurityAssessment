# PollingSiteListView
- Description: Displays a list of polling sites.
- URL: `/polling-sites/`
- HTTP Method: GET
- Request Parameters: None
- Response:
  - HTTP Status Code: 200 (OK)
  - Content: Rendered HTML template with a list of polling sites.

# PollingSiteDetailView
- Description: Shows detailed information about a specific polling site.
- URL: `/polling-sites/<polling_site_id>/`
- HTTP Method: GET
- Request Parameters:
  - `polling_site_id`: The ID of the polling site to display.
- Response:
  - HTTP Status Code: 200 (OK)
  - Content: Rendered HTML template with detailed information about the polling site.

# PollingSiteCreateView
- Description: Allows authorized users to create a new polling site.
- URL: `/polling-sites/create/`
- HTTP Method: GET, POST
- Request Parameters: None
- Response:
  - GET:
    - HTTP Status Code: 200 (OK)
    - Content: Rendered HTML template with a form to create a new polling site.
  - POST:
    - HTTP Status Code: 302 (Found)
    - Redirect: `/polling-sites/<new_polling_site_id>/`

# PollingSiteUpdateView
- Description: Allows authorized users to update the details of a polling site.
- URL: `/polling-sites/<polling_site_id>/update/`
- HTTP Method: GET, POST
- Request Parameters:
  - `polling_site_id`: The ID of the polling site to update.
- Response:
  - GET:
    - HTTP Status Code: 200 (OK)
    - Content: Rendered HTML template with a form to update the polling site details.
  - POST:
    - HTTP Status Code: 302 (Found)
    - Redirect: `/polling-sites/<polling_site_id>/`

# PollingSiteDeleteView
- Description: Allows authorized users to delete a polling site.
- URL: `/polling-sites/<polling_site_id>/delete/`
- HTTP Method: GET, POST
- Request Parameters:
  - `polling_site_id`: The ID of the polling site to delete.
- Response:
  - GET:
    - HTTP Status Code: 200 (OK)
    - Content: Rendered HTML template with a confirmation prompt to delete the polling site.
  - POST:
    - HTTP Status Code: 302 (Found)
    - Redirect: `/polling-sites/`