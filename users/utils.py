from django.core.mail import send_mail
from django.conf import settings    

def send_email(username,email):
    subject = 'Welcome to YALEFASCO'
    body = f'''
               Hello {username},!  your registration was successful.do reach out to us for any assistance.
                Thank you for choosing YALE AUTH APP.
            '''
    send_email(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,    
    )
