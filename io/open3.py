# with open as f
# f.readline()
with open('foo', 'r') as f:
    while True:
        r = f.readline()
        if len(r) < 1:
            break
        print(r, end='')
