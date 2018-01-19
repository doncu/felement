import smtplib
from email.mime import text
import functools

from flask import render_template_string

try:
    import uwsgi
    from uwsgidecorators import mule
except ImportError:
    def mule(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper


@mule
def send(template, context):
    email_string = render_template_string(template, **context)
    msg = text.MIMEText(email_string)
    msg['Subject'] = 'Новое обращение с сайта'
    msg['From'] = ''
    msg['To'] = ''

    smtp = smtplib.SMTP('localhost')
    smtp.send_message(msg)
    smtp.quit()
