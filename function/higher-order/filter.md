### Python __builtins__.filter()
It is sort of similar with the function map(),  
it receive two parameters, one is function,  
and another one is the sequences list.
It will filters out the seqqences list and promote a new list.
#### Just look
* remove the odd numbers and remains the even numbers from a list:
```python
>>> def is_odd(n):
...     return n % 2 == 1
... 
>>> filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
[1, 5, 9, 15]
```
* remove the blankspace strings from a list:
```python
>>> def not_empty(s):
...     return s and s.strip()
... 
>>> filter(not_empty, ['A', '', 'B', None, 'C', '  '])
['A', 'B', 'C']
```
