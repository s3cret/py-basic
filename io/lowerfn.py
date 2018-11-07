import os
path = '../oop'
os.chdir(path)
lst = [x for x in os.listdir('.') if os.path.isfile(x) and 'py' in x]
for each in lst:
    old = each
    try:
        new = each[0].lower() +  each[1:]
        print('Renaming -', old, 'to', new)
        os.rename(old, new)
    except Exception as e:
        print('Error occurs:', e)
        continue
print('Finished!')
