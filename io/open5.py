with open('foo', 'rb') as f:
    content = f.read()
    print('type:', type(content))
    print('length:', len(content))
    print(content)
