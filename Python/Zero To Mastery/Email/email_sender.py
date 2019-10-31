import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Senthil Kumar Kanagaraj'
email['to'] = 'kabil.vasu@gmail.com'
email['subject'] = 'You won $3,00,000!!!'

email.set_content("I'm a Python Guru!!!") 