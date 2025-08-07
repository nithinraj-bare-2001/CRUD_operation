# Flask MongoDB CRUD Application

This is a simple Flask REST API that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database. It manages user data with fields like name, email, and password.

## Technologies Used

- Flask (Python)
- MongoDB
- Docker and Docker Compose
- Postman (for API testing)

## Project Structure

SDE/
├── app/
│ ├── init.py
│ ├── config.py
│ ├── models/
│ │ └── user_model.py
│ ├── routes/
│ │ └── user_routes.py
├── run.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

## How to Run

1. Clone the repository:
    git clone https://github.com/nithinraj-bare-2001/CRUD_operation.git
    cd SDE

2. Build and start the application using Docker Compose:
    docker-compose up --build

3. The Flask API will be available at:  
   `http://localhost:5000`

## API Endpoints

All endpoints are under the `/users` path.

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | /users/          | Get all users         |
| GET    | /users/<id>      | Get user by ID        |
| POST   | /users/          | Create new user       |
| PUT    | /users/<id>      | Update user by ID     |
| DELETE | /users/<id>      | Delete user by ID     |


### Sample JSON Body for POST/PUT

```json
{
  "name": "Nithin",
  "email": "nithin@example.com",
  "password": "mypassword"
}

Testing
You can use Postman to send HTTP requests to the API. Make sure Docker is running and the containers are up before testing.

Notes
This is a basic setup without authentication.

Passwords are stored in plain text for simplicity (not recommended in production).

Data is stored in MongoDB in a Docker volume.

Author
Nithin Raj K
Email: nithinrajbare@gmail.com 
GitHub: https://github.com/nithinraj-bare-2001
