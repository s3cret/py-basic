from email.parser import Parser
import poplib
import json
with open('key.json', 'r') as f:
    content = f.read()
    keys = json.loads(content)
    email = keys['email']
    password = keys['password']
    pop3_server = keys['pop3_server']
    pop3_port = keys['pop3_port']

server = poplib.POP3_SSL(pop3_server)
# server.set_debuglevel(1)
print(server.getwelcome())
server.user(email)
server.pass_(password)
print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
index = len(mails)
resp, lines, octets = server.retr(index)
print(type(lines[0]))
msg_content = b'\r\n'.join(lines).decode()
msg = Parser().parsestr(msg_content)
# server.del(index)
server.quit()
print(msg)
# next is all the decode things using mail module
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
# ...
