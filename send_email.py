
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail ,Email

# Your verified sender
SENDGRID_API_KEY = "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"
FROM_EMAIL = Email("b231160@skit.ac.in","LIFE_CONNECT")   # ✅ must be verified sender

def send_email(subject, to_emails, body):
    """
    Send email via SendGrid
    :param subject: Email subject
    :param to_emails: list of recipient emails
    :param body: HTML email content
    """
    if not isinstance(to_emails, list):
        to_emails = [to_emails]

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        for email in to_emails:
            message = Mail(
                from_email=FROM_EMAIL,
                to_emails=email,
                subject=subject,
                html_content=body  # ✅ supports HTML formatting
            )
            response = sg.send(message)
            print(f"📩 Email sent to {email}! Status: {response.status_code}")
    except Exception as e:
        print("❌ Error while sending email:", e)
