from django.conf import settings
from django.core.mail import send_mail


def send_email_user(data):
    # print(f"Здравствуйте, {data['name']}\n Ваш вопрос получен. Ответ будет выслан на электронную почту {data['email']}.\nВаш вопрос:\n{data['message_text']}")
    send_mail(
        'Вопрос на сайте SuperSchool получен',
        f"Здравствуйте, {data['name']}\nВаш вопрос получен. Ответ будет выслан на эту электронную почту.\nВаш вопрос:\n{data['message_text']}",
        settings.EMAIL_HOST_USER,
        [data['email']],
        fail_silently=False,
    )


'''def send_email_admin(data):
    print(f"От посетителя сайта {data['name']} ({data['email']}) поступил вопрос:\n{data['message_text']}")
    mail_admins(
        f"Вопрос с сайта! {data['topic']}",
        f"От посетителя сайта {data['name']} ({data['email']}) поступил вопрос:\n{data['message_text']}",
        fail_silently=False,
    )'''
