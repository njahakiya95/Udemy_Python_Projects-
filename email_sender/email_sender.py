import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Nick P'
email['to'] = 'plnick1135@gmail.com'
email['subject'] = 'You have won $1000'

email.set_content('I am a Python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('', '!')
	smtp.send_message(email)
