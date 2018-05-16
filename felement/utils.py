import smtplib
from email.mime.text import MIMEText

from flask import render_template


def send_email(host, log_pass, subject, from_, to, template, **kwargs):
    smtp = smtplib.SMTP_SSL(host=host, timeout=1)
    smtp.login(*log_pass)

    email_string = render_template(template, **kwargs)
    msg = MIMEText(email_string, 'html')
    msg['Subject'] = subject
    msg['From'] = from_
    msg['To'] = to

    smtp.send_message(msg)
    smtp.quit()
