import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "enrique.a.lau@gmail.com"
    msg['from'] = user
    password = 'rmqkcxjsigwcoqnn'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

if __name__ == '__main__':
    email_alert("Price Change", "https://ammoseek.com/ammo/9mm-luger", "contact@countyarmament.com")
