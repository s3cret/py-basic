from collections import Counter
c = Counter()
for each in 'programmingbanana':
    c[each] = c[each] + 1

print(c)
print(c['a'])
