# Task Tracker API

A simple RESTful API built with Python and Flask to manage a to-do list. This project is part of the Junior Developer Skills Assessment for TSA Group.

## Project Overview

This API allows users to create, read, update, and delete tasks. Tasks are stored in-memory during runtime (no database required), demonstrating basic REST API design and Python Flask skills.

## Tech Stack

- **Python 3** — chosen for readability and beginner-friendliness  
- **Flask** — lightweight web framework, easy to set up and ideal for REST APIs  

## API Endpoints

| Method | Endpoint        | Description                     | Request Body Example                | Response                     |
|--------|-----------------|---------------------------------|------------------------------------|------------------------------|
| GET    | `/tasks`        | Retrieve all tasks               | N/A                              | List of task objects          |
| POST   | `/tasks`        | Create a new task                | `{ "title": "Buy groceries" }`   | Created task object           |
| PUT    | `/tasks/:id`    | Update task (title or completed) | `{ "title": "New title", "completed": true }` | Updated task object           |
| DELETE | `/tasks/:id`    | Delete a task                   | N/A                              | No content (204)              |

## How to Run

### Locally (if you have Python installed)

1. Clone the repo:  
   ```bash
   git clone https://github.com/fifidonnelly/task-tracker-api.git
   cd task-tracker-api 
   ```

2. Create a virtual environment:
    ```bash 
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    python app.py 
    ```

5. Open your browser or API client and use the endpoints at:  
`http://127.0.0.1:5000`

## Online (via GitHub Codespaces or Replit)
You can run this project in an online IDE that supports Python and Flask without installing anything locally.

## Bonus Features
- In-memory persistence using a Python list to store tasks during runtime  
- Input validation on POST and PUT requests, including checks for empty titles and correct data types  
- Clear and consistent HTTP status codes and descriptive error messages  
- Unit tests covering core API endpoints using Python's `unittest` framework  


## Future Improvements (Optional)

- Persist tasks to a database instead of in-memory storage  
- Add user authentication and authorization  
- Develop a frontend interface with animations for task management  

