try:
    print('try ...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('This is the finally part running.')
print('END')
