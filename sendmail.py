import smtplib

from_addr= ''
to_addr = 'david@someemail.com'

message= """
From: {} <{}> 
To: {}<{}> 
subject: {}

{}
"""
from_name='James'
to_name="paul"
subject="Test"
msg="It Works!"
message_to_send = message.format(from_name, from_addr,to_name, to_addr, subject,msg)

username=''
password=''

server= smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(from_addr,to_addr,message_to_send)
server.quit()