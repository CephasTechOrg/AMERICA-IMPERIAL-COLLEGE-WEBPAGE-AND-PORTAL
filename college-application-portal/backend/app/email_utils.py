import os
import smtplib
from email.message import EmailMessage

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def send_email(to_address: str, subject: str, body: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_address
    msg.set_content(body)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

def send_confirmation_to_student(app):
    subject = f"Application received, ID {app.id}"
    files_text = ""
    if app.uploaded_files:
        files_text = "\nFiles:\n" + "\n".join(app.uploaded_files)
    body = (
        f"Dear {app.first_name} {app.last_name},\n\n"
        f"Your application was received.\n"
        f"Application ID: {app.id}\n"
        f"Submitted at: {app.created_at}\n\n"
        "We will review and notify you.\n\n"
        f"{files_text}\n\n"
        "Regards,\nAdmissions"
    )
    send_email(app.email, subject, body)

def notify_admissions(app):
    subject = f"New application, ID {app.id}"
    files_text = ""
    if app.uploaded_files:
        files_text = "\nFiles:\n" + "\n".join(app.uploaded_files)
    app_link = f"{BASE_URL}/dashboard/index.html"
    body = (
        f"New application received.\n\n"
        f"Name: {app.first_name} {app.last_name}\n"
        f"Email: {app.email}\n"
        f"ID: {app.id}\n\n"
        f"{files_text}\n\n"
        f"Open dashboard: {app_link}\n"
    )
    send_email(ADMIN_EMAIL, subject, body)
