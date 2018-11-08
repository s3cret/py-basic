#!/usr/bin/python3
from time import sleep
from random import random

total = 23
for i in range(23):
    cur = i + 1
    process = str(cur) + '/' + str(total)
    process_bar = '>' * cur + '-' * (total - cur) + process
    print(process_bar, '\r', end='')
    sleep_time = random()
    sleep(sleep_time)
print()
