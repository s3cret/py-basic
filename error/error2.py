try:
    print('try ...')
    r = 10 / int('it is a string. boom!')
    print('result:', r)
except ValueError as e:
    print('Error occurs:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError details:', e)
else:
    print('There is no ZeroDivisionError al all')
finally:
    print('This is the finally part going.')
print('End')
