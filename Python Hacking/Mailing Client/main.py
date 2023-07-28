import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    credentials = flow.run_local_server(port=0)

    return credentials

def main():
    credentials = get_credentials()
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls(context=context)
    server.login(credentials.client_id, credentials.client_secret)

    # Rest of your email sending code (MIME, attachments, recipients, etc.)

    server.quit()

if __name__ == "__main__":
    main()
