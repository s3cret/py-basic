from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_sender_receiver(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def main():
    smtp_server = 'smtp.163.com'
    smtp_server_port = 465
    smtp_server_port = 994
    user = 'amtcodes@163.com'
    password = ''
    receivers = ['2235861426@qq.com', '383304557@qq.com']
    with open('key', 'r') as f:
        password = f.readline().strip()

    message = '''
    send from smtplib.login(user, password)
    message is here
    and smtplib.sendmail(user, receivers, str)
    Hello, world
    finally smtplib.quit()
    '''
    message1 = '''
    This is definitly not a spam email,
    I am just learning python with the
    great smtplib module, and may send
    a few spam-like email. That's all.
    '''

    html_message = '''<html><body><h1>Hello</h1>
    <p>send by <a href="http://www.python.org">Python</a>...</p>
    </body></html>'''

    msg = MIMEText(message1, 'plain', 'utf-8')
    # msg = MIMEText(html_message, 'html', 'utf-8')
    msg['Subject'] = Header('Greetings', 'utf-8').encode()
    msg['From'] = _format_sender_receiver('Jesse <%s>' % user)
    msg['To'] = _format_sender_receiver('Receiver <%s>' % 'slt')

    try:
        # init a SMTP_SSL server
        server = smtplib.SMTP_SSL(smtp_server, smtp_server_port)
        server.login(user, password)
        server.sendmail(user, receivers, msg.as_string())
        print('Your mail has been sent successfully.')
    except Exception as e:
        print('Send email failed.')
        print('Details:', e)
    finally:
        server.quit()

main()

