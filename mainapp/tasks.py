from django.core.mail import mail_admins
from settings.celery import app

@app.task 
def send_email_admin(data):
    print(f"От посетителя сайта {data['name']} ({data['email']}) поступил вопрос:\n{data['message_text']}")
    mail_admins(
        f"Вопрос с сайта! {data['topic']}",
        f"От посетителя сайта {data['name']} ({data['email']}) поступил вопрос:\n{data['message_text']}",
        fail_silently=False,
    )