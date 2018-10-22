### Iteration
------------

#### Use `for` loop to iterate a iterable instance

```python
for char in 'ABC':
    print char
```

#### Here is how you judge an instance whether it is iterable or not:

```python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # type str
True
>>> isinstance([1, 2, 3], Iterable) # type list
True
>>> isinstance(123, Iterable) # type int
False
```

#### Here is how you `enumerate` a iterable instance using its index:

```python
items = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(items):
    # do some stuff as you wish
    print(index, value)
```

#### The last example

```python
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print x, y
...
1 1
2 4
3 9
```
