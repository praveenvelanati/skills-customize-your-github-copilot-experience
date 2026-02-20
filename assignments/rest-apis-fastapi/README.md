# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to understand HTTP methods, request handling, and API design patterns. You'll create endpoints that handle CRUD operations and return structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Initialize a FastAPI application with necessary imports and create a basic server structure that can handle HTTP requests and responses.

#### Requirements
Completed program should:

- Import FastAPI and related modules correctly
- Create a FastAPI application instance
- Define a root endpoint that returns a welcome message
- Include proper docstrings and comments explaining each section
- Run successfully with `uvicorn` server

Example:
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
```

### 🛠️ Create Resource Models and CRUD Endpoints

#### Description
Define data models using Pydantic and implement GET, POST, PUT, and DELETE endpoints for managing a collection of resources.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource (e.g., Item, Task, Product)
- Implement GET endpoint to retrieve all resources
- Implement GET endpoint with ID to retrieve a single resource
- Implement POST endpoint to create a new resource
- Implement PUT endpoint to update an existing resource
- Implement DELETE endpoint to remove a resource
- Return appropriate status codes (200, 201, 404)

Example response format:
```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "A sample resource"
}
```

### 🛠️ Add Input Validation and Error Handling

#### Description
Implement request validation using Pydantic models and add error handling to provide meaningful error messages to API clients.

#### Requirements
Completed program should:

- Validate input data using Pydantic models
- Return HTTP 400 error for invalid requests
- Return HTTP 404 error when resource not found
- Include custom error messages that describe what went wrong
- Handle edge cases gracefully
- Test endpoints using documentation UI (Swagger or ReDoc)
