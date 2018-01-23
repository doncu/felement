import smtplib
from email.mime import text

from flask import render_template_string


def send_email(host, log_pass, subject, from_, to, template, **kwargs):
    smtp = smtplib.SMTP_SSL(host=host, timeout=1)
    smtp.login(*log_pass)

    email_string = render_template_string(template, **kwargs)
    msg = text.MIMEText(email_string)
    msg['Subject'] = subject
    msg['From'] = from_
    msg['To'] = to

    smtp.send_message(msg)
    smtp.quit()
