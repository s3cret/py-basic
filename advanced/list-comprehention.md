### List Comprehension
----------------------

#### use range
To generate a list looks like [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use range():

```python
mylist = range(1, 11)
```

> #### What if the list looks like [1x1, 2x2, 3x3, ..., 10x10] ?
```python
>>> mylist = []
>>> for x in range(1, 11):
...    mylist.append(x * x)
...
>>> mylist
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

#### When you use `list comprehension`

It will just use one line as below
```python
mylist = [ x * x for x in range(1, 11) ]
```
> You can also add if judgement to generate your list more precisely
```python
>>> [ n * n for n in range(1, 11) if n % 2 ==0 ]
[4, 16, 36, 64, 100]
```
or
```python
>>> [ m + n for m in 'ABC' for n in 'DEF' ]
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

#### Examples of list comprehension
* List all the file in present working dirctory
    ```python
import os
dirs = [ d for d in os.listdir('.') ]
```

* Lower each single character in a list
    ```python
lowers = [ s.lower() for s in list ]
```

* Final interest
You will certainly get a traceback when you call lower() for the `int` Object
    ```python
>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'lower'
```

Here is how to fix that:
```python
fixlist = [ s.lower for s in L if isinstance(s, str) ]
```
