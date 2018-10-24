#!/usr/bin/python3
from time import sleep

total = 23
for i in range(23):
    cur = i + 1
    process = str(cur) + '/' + str(total)
    process_bar = '>' * cur + '-' * (total - cur) + process
    print(process_bar, '\r', end='')
    sleep(0.08)
print()
