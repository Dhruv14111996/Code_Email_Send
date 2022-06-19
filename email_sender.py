import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Dhruv Shah'
email['to'] = 'patelmansib2707@gmail.com'
email['subject'] = 'Today you have Mihil classes at 3pm.'

email.set_content = 'Hello Mansi patle. \nGood afternoon. \n Here you have reminder that today you have mihile calsses and dont forget to attend that. If you dont attend then you did not pass exam.'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dhruvzerotomastery123@gmail.com', 'Dhruv@123456')
    smtp.send_message(email)
    print('Everything is Good!')
