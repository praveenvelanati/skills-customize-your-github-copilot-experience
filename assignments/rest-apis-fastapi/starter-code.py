"""
REST APIs with FastAPI - Starter Code

This is a starter template for building a RESTful API with FastAPI.
Follow the assignment requirements to implement the missing functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(title="My REST API", version="1.0.0")

# TODO: Define a Pydantic model for your resource
# Example structure (replace with your own):
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# TODO: Create a simple in-memory database (list) to store resources
# Example: items_db = []


# TODO: Implement the GET root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint - returns a greeting message"""
    # IMPLEMENT: Return a welcome message
    pass


# TODO: Implement GET endpoint to retrieve all resources
@app.get("/items")
def get_items():
    """Retrieve all items from the database"""
    # IMPLEMENT: Return all items from your database
    pass


# TODO: Implement GET endpoint to retrieve a single resource by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    # IMPLEMENT: Find and return the item with the given ID
    # IMPLEMENT: Raise HTTPException with 404 if not found
    pass


# TODO: Implement POST endpoint to create a new resource
@app.post("/items")
def create_item(item):
    """Create a new item"""
    # IMPLEMENT: Add the item to your database
    # IMPLEMENT: Return the created item with appropriate status code
    pass


# TODO: Implement PUT endpoint to update an existing resource
@app.put("/items/{item_id}")
def update_item(item_id: int, item):
    """Update an existing item"""
    # IMPLEMENT: Find the item by ID
    # IMPLEMENT: Update its properties
    # IMPLEMENT: Return the updated item or raise HTTPException if not found
    pass


# TODO: Implement DELETE endpoint to remove a resource
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item"""
    # IMPLEMENT: Find and remove the item from the database
    # IMPLEMENT: Return a confirmation message or raise HTTPException if not found
    pass


# To run this application, use:
# uvicorn starter-code:app --reload
