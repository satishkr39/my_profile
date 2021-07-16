# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("satishsinghkumarr@gmail.com", "Satishsinghkumarrtest")

# message to be sent
text = "hi this is test message from python"
subject = "This is subject from python"
message = 'Subject: {}\n\n{}'.format(subject, text)
# sending the mail
s.sendmail("satissinghkumarr@gmail.com", "satishkr639@gmail.com", message)

# terminating the session
s.quit()