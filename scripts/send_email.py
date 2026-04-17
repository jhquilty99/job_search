import smtplib, os, sys, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / '.env')

SENDER = RECIPIENT = 'jhquilty99@gmail.com'
DRAFT_FILE = Path(__file__).parent / 'email_draft.json'

password = os.environ.get('GMAIL_APP_PASSWORD')
if not password:
    print('ERROR: GMAIL_APP_PASSWORD not set')
    print()
    print('To fix this:')
    print('  1. Go to myaccount.google.com/apppasswords')
    print('  2. Generate an App Password for "Mail"')
    print('  3. Set GMAIL_APP_PASSWORD in your .env file')
    sys.exit(1)

if not DRAFT_FILE.exists():
    print(f'ERROR: {DRAFT_FILE} not found — skill must write email_draft.json first')
    sys.exit(1)

draft = json.loads(DRAFT_FILE.read_text(encoding='utf-8'))

msg = MIMEMultipart('alternative')
msg['Subject'] = draft['subject']
msg['From'] = SENDER
msg['To'] = RECIPIENT
msg.attach(MIMEText(draft['plain'], 'plain'))
msg.attach(MIMEText(draft['html'], 'html'))

with smtplib.SMTP('smtp.gmail.com', 587) as s:
    s.ehlo()
    s.starttls()
    s.login(SENDER, password)
    s.sendmail(SENDER, RECIPIENT, msg.as_string())

DRAFT_FILE.unlink()

print(f'Email sent to {RECIPIENT}')
print(f'Subject: {draft["subject"]}')
