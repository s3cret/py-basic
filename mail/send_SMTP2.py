from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    '''returns an email.Header object'''
    # print(s)
    # actually it splits the string with delimiter <>
    # a <b>
    name, addr = parseaddr(s)
    # print('name:', name)
    # print('address:', addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def main():
    # user = input('Username: ')
    user = 'amtcodes@163.com'
    # password = input('Password: ')
    password = ''
    with open('key', 'r') as f:
        password = f.readline().strip()

    # init a MIMEText instance assign it to variable msg
    message = 'Send from python smtplib.SMTP_SSL.login()\nsmtplib.SMTP_SSL.sendmail()'
    msg = MIMEText(message, 'plain', 'utf-8')
    # set the MIMEText's Header element: Subject
    msg['Subject'] = Header('Hello Again From SMTP greet ...', 'utf-8').encode()

    # set the sender, Header object
    msg['From'] = _format_addr('Python learner <%s>' % user)

    # set the receiver, Header object, maybe not useful
    # this mostly will be force replaced by the mailserver
    # the receiver use with the receiver's name<address>
    # to = input('To: ')
    # people you want to send to
    to0 = '2235861426@qq.com'
    to = '383304557@qq.com'
    receivers = list()
    receivers.append(to0)
    receivers.append(to)

    msg['To'] = _format_addr('Receiver <%s>' % to)

    # set SMTP server
    # smtp_server = input('SMTP server: ')
    smtp_server = 'smtp.163.com'

    # msg is an instance of MIMEText, which is formatted already
    # print('--- MIMEText begin ---')
    # print(msg)
    # print('--- MIMEText end   ---')

    # init the SMTP_SSL server
    server = smtplib.SMTP_SSL(smtp_server, 465)
    #server.starttls()
    # this would print all the debug information
    # server.set_debuglevel(1)
    server.login(user, password)
    # sender, receivers, as_string() turns the formatted msg to string
    server.sendmail(user, receivers, msg.as_string())
    server.quit()

main()
