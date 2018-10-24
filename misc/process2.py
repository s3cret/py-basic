#!/usr/local/bin/python3
total = 24
for i in range(total):
    count = i + 1
    number = round(count/total, 2)
    percent = str(number * 100) + "%"
    print(count, '/', total, '=', percent)
