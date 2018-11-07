with open('foo', 'r') as f:
    while True:
        r = f.read(1)
        if len(r) < 1:
            break
        # " " is 32, "\n" is 10
        #print('r.read(1):', ord(r))
        print('r.read(1):', r)
