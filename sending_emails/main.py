import smtplib
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
email = input('Email : ')
password = input('what is your password')
print(smtp_object.login(email, password))
from_address = email
to_address = email
subject = input('enter a subject line')
message = input('enter the body message')
msg = "Subject: "+subject+'\n'+message
smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()
