from src import app, mail
import smtplib, ssl
from flask_mail import Message


class Email:
    @staticmethod
    def send_by_email(email_addresses: list[str], message_body: str):
        msg = Message('Accounting Application', sender=app.config['MAIL_USERNAME'], recipients=email_addresses)
        msg.html = message_body
        mail.send(msg)
