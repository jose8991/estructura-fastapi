import smtplib
from email.mime.text import MIMEText

def send_email(to_email: str, subject: str, body: str):
    from_email = "your-email@example.com"
    password = "your-email-password"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())