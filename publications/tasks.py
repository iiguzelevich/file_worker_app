from config.celery import app
from django.core.mail import send_mail


@app.task
def send_letter(_mail):
    mail = send_mail(
        'New publication',
        'The user you are subscribed to has published a new file',
        'ii',
        _mail
    )
    return mail
