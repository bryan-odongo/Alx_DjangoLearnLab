---

# Social Media API

---

## Project Overview

This **Social Media API** is designed to provide backend functionality for a social media platform. It supports user registration, post management, follower relationships, and personalized feeds. The API adheres to RESTful principles and is built using Django's ORM and DRF for efficient database interactions and secure authentication.

---

## Features

### Post Management
- **Create**: Authenticated users can create posts with text content and optional media (e.g., image URLs).
- **Read**: Retrieve individual posts or a list of all posts.
- **Update**: Users can update their own posts.
- **Delete**: Users can delete their own posts.
- **Validation**: Ensures required fields like `Content` and `User` are validated.

### User Management
- **Register**: Users can register with a unique username, email, password, and optional profile fields (bio, profile picture).
- **Profile**: Retrieve user details, including their posts and follower/following count.
- **Update Profile**: Users can update their profile information.
- **Delete Account**: Users can delete their account.

### Follow System
- **Follow/Unfollow**: Users can follow or unfollow other users.
- **Validation**: Prevents users from following themselves.
- **Relationship Tracking**: Efficiently tracks follower and following relationships.

### Feed of Posts
- **Personalized Feed**: Displays posts from users the authenticated user follows, sorted in reverse chronological order.
- **Filtering**: Optionally filter posts by date or search by keyword.
- **Pagination**: Handles large datasets with paginated responses.

---

## API Endpoints

| Endpoint                     | HTTP Method | Description                                   | Authentication Required |
|------------------------------|-------------|-----------------------------------------------|--------------------------|
| `/api/register/`             | POST        | Register a new user                           | No                       |
| `/api/login/`                | POST        | Authenticate and log in a user                | No                       |
| `/api/users/<int:user_id>/`  | GET         | Retrieve user details                         | Yes                      |
| `/api/users/<int:user_id>/`  | PUT         | Update user profile                           | Yes                      |
| `/api/users/<int:user_id>/`  | DELETE      | Delete user account                           | Yes                      |
| `/api/posts/`                | GET         | List all posts                                | No                       |
| `/api/posts/`                | POST        | Create a new post                             | Yes                      |
| `/api/posts/<int:post_id>/`  | GET         | Retrieve a specific post                      | No                       |
| `/api/posts/<int:post_id>/`  | PUT         | Update a specific post                        | Yes                      |
| `/api/posts/<int:post_id>/`  | DELETE      | Delete a specific post                        | Yes                      |
| `/api/follow/<int:user_id>/` | POST        | Follow a user                                 | Yes                      |
| `/api/unfollow/<int:user_id>/`| POST       | Unfollow a user                               | Yes                      |
| `/api/feed/`                 | GET         | View personalized feed of followed users' posts | Yes                  |

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended)
- PostgreSQL or SQLite (for database)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/social-media-api.git
   cd social-media-api
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be accessible at `http://localhost:8000`.

---

## Authentication

- **Token-Based Authentication (JWT)**:
  - Use the `/api/login/` endpoint to authenticate and receive a JWT token.
  - Include the token in the `Authorization` header for authenticated requests:
    ```
    Authorization: Bearer <your_token>
    ```

- **Session-Based Authentication**:
  - For local development, session-based authentication is also supported.

---

## Deployment

### Deployment Instructions

1. **Prepare for Deployment**
   - Install production dependencies:
     ```bash
     pip install gunicorn whitenoise
     ```
   - Collect static files:
     ```bash
     python manage.py collectstatic
     ```

2. **Deploy to Heroku**
   - Push the code to Heroku:
     ```bash
     git push heroku main
     ```
   - Run migrations on Heroku:
     ```bash
     heroku run python manage.py migrate
     ```

3. **Deploy to PythonAnywhere**
   - Upload the project files to PythonAnywhere.
   - Configure the WSGI file to point to your Django application.

4. **Environment Variables**
   - Set environment variables for sensitive data (e.g., `SECRET_KEY`, database credentials).

---
