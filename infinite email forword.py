import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.example.com' 
IMAP_SERVER = 'imap.example.com'   
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

def forward_email(subject, body, to_address, times):
    for _ in range(times):
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f'Forwarded email to {to_address}')

def fetch_latest_email():
    with imaplib.IMAP4_SSL(IMAP_SERVER) as mail:
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mail.select('inbox')

        result, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        if email_ids:
            latest_email_id = email_ids[-1]
            result, data = mail.fetch(latest_email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg['subject']
            body = msg.get_payload(decode=True).decode()

            return subject, body
        else:
            print("No emails found.")
            return None, None

#if _name_ == '_main_':
    subject, body = fetch_latest_email()
    if subject and body:
        forward_email(subject, body, 'recipient@example.com', 5)  #Forward 5 times
