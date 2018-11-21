from email.encoders import encode_base64
from email.header import Header
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

user = 'amtcodes@163.com'
password = ''
with open('key', 'r') as f:
    password = f.readline().strip()
smtp_server = 'smtp.163.com'
receivers = ['2235861426@qq.com', '383304557@qq.com']

def _format_sender_and_receivers(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEMultipart()
# for sending both plain type and html type
# set the subtype to be alternative
msg = MIMEMultipart('alternative')
msg['Subject'] = Header('SMTP Attachment', 'utf-8').encode()
msg['From'] = _format_sender_and_receivers('Python learner <%s>' % user)
msg['To'] = _format_sender_and_receivers('Receiver <%s>' % receivers[0])

message = MIMEText('Hello, this is the message content.', 'plain', 'utf-8')
html = '''<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'''
html_message = MIMEText(html, 'html', 'utf-8')
with open('zhihu.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='yeszhihu.png')
    # three lines of essential mime header
    mime.add_header('Content-Disposition', 'attachment', filename='yeszhihu.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encode_base64(mime)

msg.attach(message)
msg.attach(html_message)
msg.attach(mime)

import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465)
server.login(user, password)
server.sendmail(user, receivers, msg.as_string())
server.quit()
