from celery import Celery
from datetime import datetime, timedelta
from app.models import Task
from app.utils.database import get_db_session
from app.services.email_service import send_email

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def send_task_reminders():
    session = get_db_session()
    try:
        now = datetime.utcnow()
        one_day_later = now + timedelta(days=1)

        # Query for tasks due in the next 24 hours
        tasks = session.query(Task).filter(
            Task.due_date.between(now, one_day_later),
            Task.status == False
        ).all()

        for task in tasks:
            user = task.owner
            send_email(
                to_email=user.username,  # Assuming username is the email address
                subject=f"Reminder: Task '{task.title}' is due soon",
                body=f"Your task '{task.title}' is due on {task.due_date}. Please complete it."
            )

    except Exception as e:
        print(f"Error in sending reminders: {e}")
    finally:
        session.close()
