

# These imports are pre-installed with Python
from email.message import EmailMessage # Here we head over to our gmail account and ensure that 2-factor authentication has been set up

from email_password import password # Calling password from email_password.py class
import ssl
import smtplib

email_sender = 'originthoughts21@gmail.com' #
email_password = password

email_receiver = 'yegapa4966@esterace.com' # The string in this variable can be replaced with any existing email or temporary email which will serve as a receiver for this mail.
subject = "Test to receive email" # This variable contains the string that will be used in the subject line of the sending email.
# This string variable contains triple quotes which allows you to use line breaks between text and will serve as the body of the email.
body = """ 
This is an broadcast coming from the aliens in outer space, prepare to be turned into fruit and nut chocolate!

Kind Regards,
E.T.
"""
# An instance of the email sender is created which gets initialized to the senders email, the receivers email, the subject line and the body.
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# This allows python to log in to the email and the mail using the email variables
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())