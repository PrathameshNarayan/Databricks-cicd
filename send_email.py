import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Get GitHub Actor and Commit Message
actor = os.getenv('GITHUB_ACTOR')
commit_message = os.getenv('GITHUB_COMMIT_MESSAGE')

# Email details
sender_email = os.getenv('OUTLOOK_EMAIL')
receiver_email = os.getenv('MAIN_BRANCH_OWNER_EMAIL')  # Owner email from secret
password = os.getenv('OUTLOOK_PASSWORD')

# Email content
subject = "New commit pushed to main branch"
body = f"""
Hello,

A new commit has been pushed to the 'main' branch by {actor}.

Commit Message:
{commit_message}

Best regards,
Your GitHub Actions CI
"""

# Setup the MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# SMTP server configuration
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
