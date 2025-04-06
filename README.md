Event Management API


Overview


This is a Django-based API for managing events. It provides functionality for event creation, registration, user registration, event categories, locations, and authentication. The API supports JWT (JSON Web Token) authentication for secured access.

Features


User Registration: Register new users using a secure password.

Event Management:Create, retrieve, update, and delete events.

Event Registration: Users can register for events, ensuring that the event does not exceed its capacity.

Category and Location Management: Categorize and assign locations to events.

JWT Authentication: Secure endpoints using JWT tokens.

Event Filtering: Filter events by title, location, and category.

Technologies Used

Backend Framework: Django 5.x

API Framework: Django REST Framework

Authentication: JWT (JSON Web Tokens) with rest_framework_simplejwt

Filtering: django-filter for advanced query filtering

Database: SQLite (default) or can be configured to use other databases

Other Dependencies:

djangorestframework

django-filter

djangorestframework-simplejwt

API Endpoints

1. User Registration
URL: /api/user/register/

Method: POST

Request Body:

json

{
    "username": "new_user",
    "email": "user@example.com",
    "password": "password123"
}
Response:

json

{
    "message": "User created successfully"
}
Description: Allows users to register with a username, email, and password.

2. User Login

URL: /api/user/login/

Method: POST

Request Body:

json

{
    "username": "new_user",
    "password": "password123"
}
Response:

json

{
    "access": "your_access_token_here"
}
Description: Authenticates the user and returns a JWT token for subsequent requests.

3. Event Management

List Events
URL: /api/events/

Method: GET

Response:

json

[
    {
        "id": 1,
        "title": "Event Title",
        "location": "Location Name",
        "date_time": "2025-04-10T15:00:00Z",
        "organizer": "username",
        "category": "Category Name",
        "capacity": 100
    }
]
Description: Retrieves a list of events. Filters can be applied using query parameters.

Create Event
URL: /api/events/

Method: POST

Request Body:

json

{
    "title": "New Event",
    "description": "new event",
    "location": 1,
    "date_time": "2025-04-20T09:00:00Z",
    "category": 1,
    "capacity": 200
}
Response:

json

{
    "id": 1,
    "title": "New Event",
    "description": "new event",
    "location": "Location Name",
    "date_time": "2025-04-20T09:00:00Z",
    "organizer": "username",
    "category": "Category Name",
    "capacity": 200
}
Description: Allows authenticated users to create a new event.

Retrieve, Update, Delete Event
URL: /api/events/{event_id}/

Methods:

GET: Retrieve event details.

PUT: Update event details.

DELETE: Delete the event.

Response for GET:

json

{
    "id": 1,
    "title": "Event Title",
    "location": "Location Name",
    "date_time": "2025-04-10T15:00:00Z",
    "organizer": "username",
    "category": "Category Name",
    "capacity": 100
}
Response for PUT:

json

{
    "message": "Event updated successfully"
}
Description: Allows authenticated users to retrieve, update, or delete events they created.

4. Event Registration

URL: /api/register/

Method: POST

Request Body:

json

{
    "event": 1
}
Response:

json

{
    "message": "Successfully registered for the event."
}
Description: Allows users to register for an event. It ensures the event doesn’t exceed its capacity.

5. Category List

URL: /api/categories/

Method: GET

Response:

json

[
    {
        "id": 1,
        "name": "Technology"
    },
    {
        "id": 2,
        "name": "Business"
    }
]
Description: Retrieves a list of event categories.

6. Location List

URL: /api/locations/

Method: GET

Response:

json

[
    {
        "id": 1,
        "name": "Location Name",
        "address": "123 Event St, City, Country"
    }
]
Description: Retrieves a list of event locations.

Authentication
This API uses JWT (JSON Web Token) authentication.

Obtain JWT Token: After successful login, a JWT token is returned. The token must be included in the Authorization header for any protected endpoints.

Example:

text
Copy
Authorization: Bearer your_access_token_here
Token Expiration: JWT tokens are valid for a certain period (e.g., 1 hour). After expiration, the user must log in again to obtain a new token.

Dependencies
Make sure to install the required dependencies:

bash
Copy
pip install -r requirements.txt
The requirements.txt should contain:

shell
Copy
Django>=5.1
djangorestframework>=3.14
djangorestframework-simplejwt>=5.0
django-filter>=23.0
Setup Instructions
Clone the repository:

bash
Copy
git clone https://github.com/mahlet-16/EventManagement_api.git
cd EventManagement_api
Install dependencies:

bash
Copy
pip install -r requirements.txt
Apply migrations:

bash
Copy
python manage.py migrate
Run the development server:

bash
Copy
python manage.py runserver
Access the API: You can now access the API at http://127.0.0.1:8000/.

Example Usage
Register a user:

bash
Copy
curl -X POST http://127.0.0.1:8000/api/user/register/ \
-H "Content-Type: application/json" \
-d '{"username": "user1", "email": "user1@example.com", "password": "password123"}'
Login to get the JWT token:

bash
Copy
curl -X POST http://127.0.0.1:8000/api/user/login/ \
-H "Content-Type: application/json" \
-d '{"username": "user1", "password": "password123"}'
Response:

json
Copy
{
    "access": "your_access_token_here"
}
Create an event (using the token in Authorization header):

bash
Copy
curl -X POST http://127.0.0.1:8000/api/events/ \
-H "Authorization: Bearer your_access_token_here" \
-H "Content-Type: application/json" \
-d '{"title": "New Event", "location": 1, "date_time": "2025-04-20T09:00:00Z", "category": 1, "capacity": 200}'
