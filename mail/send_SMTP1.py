'''SMTP ( Simple Mail Transform Protocol )
is an Internet standard for electronic mail(email) transmission.
First defined by RFC 821 in 1982, it was updated in 2008 with
Extended SMTP addtions by RFC 5321, which is the protocol in
widespread use today.

MIME ( Multipurpose Internet Mail Extensions )
is an Internet standard that extends the format of email to support:
    Text in character sets other than ASCII
    Non-text attachments: audio, video, images, application, programs, etc
    Message bodies with multiple parts
    Header information in non-ASCII character sets
Virturally all human-written Internet email and a fairly large
proportion of automated emain is transmitted via SMTP in MIME format.
'''
# print(__doc__)
from email.mime.text import MIMEText
# the first argument is message itself
# the second is MIME subtype
# and the third is the text encoding, use utf-8 in order to grant
# the compatible of multi-language
msg = MIMEText('Hello, send by Python ...', 'plain', 'utf-8')

# user = input('From: ')
password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

user = 'amtcodes@163.com'
to_addr = '2235861426@qq.com'
smtp_server = 'smtp.163.com'

import smtplib
def main():
    '''
    write MUA(Mail User Agent) to send email
    to MTA(Mail Transfer Agent)
    '''
    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1) shows all the interactive
    # informations with the SMTP server
    server.set_debuglevel(1)
    # you can see it from the function name
    server.login(user, to_addr)
    # you can send to servral people so the argument type is list
    # as_string() turns a MIMEText object to string object
    server.sendmail(user, [to_addr], msg.as_string())
    # shutdown the server
    server.quit()

main()
