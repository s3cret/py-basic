import hashlib

md5 = hashlib.md5()
# Unicode-objects must be encoded before hashing
md5.update('how to use hashlib.md5 in python3?'.encode())
print(md5.hexdigest())

md5 = hashlib.md5()
# Unicode-objects must be encoded before hashing
md5.update('how to use hashlib.md5 in python3 ?'.encode())
print(md5.hexdigest())

# use hashlib.md5 for password hiding in the databases
salt = 'tlas'
db = {}

def register(username, password):
    # ...
    db['password'] = getmd5(username, password, salt)
