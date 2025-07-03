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

## How to Run in GitHub Codespaces

1. Open the repository in GitHub Codespaces by clicking the green **Code** button on GitHub, then **Codespaces** → **Create codespace on main**.

2. In the Codespaces terminal, install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the flask app:

    ``` bash
    python app.py
    ```

4. The app is configured to listen on all network interaces and port 5000: 

    ``` python
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
    ```

5. Click the Ports tab in Codespaces and click the link next to port 5000 to open your running API in a browser. The URL will look like:  
    `https://cautious-winner-9vp9975jpgj37v6v-5000.app.github.dev/`

 **Important:** If the link does not open or shows a 404 error, ensure port 5000 is set to **Public**:  
   - Click the gear icon next to the port in the Ports tab  
   - Set the visibility to **Public**

6. Use this URL with your API endpoints: 
    ```http
    GET https://cautious-winner-9vp9975jpgj37v6v-5000.app.github.dev/tasks
    ```

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

## Testing

All API endpoints have been manually tested using [Postman](https://www.postman.com/), a popular API client. This includes creating, reading, updating, and deleting tasks to ensure the API behaves as expected.


