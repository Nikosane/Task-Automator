# Task Automator

## Overview
**Task Automator Pro** is a task management system that allows users to manage their daily tasks through a RESTful API. It features automated email reminders for pending tasks and ensures seamless integration with PostgreSQL and Celery for automation. The project is designed for scalability and ease of deployment.

---

## Features
1. **User Management**:
   - User registration and login with JWT authentication.
   - Password hashing for security.

2. **Task Management**:
   - CRUD operations for tasks.
   - Task attributes: title, description, due date, and status (pending/completed).

3. **Automation**:
   - Automated email reminders for pending tasks.
   - Celery-based task scheduling for background jobs.

4. **Database**:
   - PostgreSQL for data persistence.

5. **API Documentation**:
   - Auto-generated Swagger documentation (if using FastAPI).

6. **Deployment**:
   - Dockerized setup with `docker-compose`.

---

## Tech Stack
### **Backend**
- **FastAPI**: For building the RESTful API.
- **SQLAlchemy**: ORM for PostgreSQL database integration.
- **Pydantic**: For data validation and serialization.
- **JWT**: Secure user authentication.

### **Automation**
- **Celery**: Task queue for background jobs.
- **Redis**: Message broker for Celery.
- **SMTP/SendGrid**: For email reminders.

### **Deployment**
- **Docker**: Containerization for application and services.
- **Docker Compose**: To manage multi-container setup.

---

## Installation

### **Prerequisites**
- Python 3.9+
- Docker & Docker Compose installed.
- Redis and PostgreSQL set up locally or accessible remotely.

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/Nikosane/task-automator.git
   cd task-automator
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the root directory.
   - Add the following:
     ```env
     DATABASE_URL=postgresql://username:password@localhost/db_name
     REDIS_URL=redis://localhost:6379/0
     EMAIL_HOST=smtp.gmail.com
     EMAIL_PORT=587
     EMAIL_USER=your-email@gmail.com
     EMAIL_PASSWORD=your-email-password
     JWT_SECRET=your-secret-key
     ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the application (development):
   ```bash
   uvicorn app.main:app --reload
   ```

7. Start Celery worker:
   ```bash
   celery -A app.services.task_scheduler worker --loglevel=info
   ```

8. Access the API:
   - Base URL: `http://localhost:8000`
   - Swagger UI: `http://localhost:8000/docs`

---

## Usage

### **Endpoints**
1. **User Management**:
   - `POST /register`: Register a new user.
   - `POST /login`: Login and receive a JWT token.

2. **Task Management**:
   - `GET /tasks`: Retrieve all tasks.
   - `POST /tasks`: Create a new task.
   - `PUT /tasks/{task_id}`: Update an existing task.
   - `DELETE /tasks/{task_id}`: Delete a task.

3. **Automation**:
   - Reminders are sent daily for pending tasks.

---

## Testing

1. Install testing dependencies:
   ```bash
   pip install pytest pytest-cov
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. View test coverage:
   ```bash
   pytest --cov=app
   ```

---

## Deployment

1. Build and run with Docker:
   ```bash
   docker-compose up --build
   ```

2. Access the application:
   - API: `http://localhost:8000`
   - Swagger UI: `http://localhost:8000/docs`

---

## Contributing

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

