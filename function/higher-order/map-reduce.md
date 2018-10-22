### map() & reduce()
--------------------

#### What is `map()`?
Function map() receive two parameters, one is function, one is sequence.  
Just do a mapping work using the given function.

```python
>>> def f(x):
...    return x * x
...
>>> map(f, [1, 2, 3, 4])
[1, 4, 9, 16]

You can also do it using a `for` loop. However, you cannot understand the meaning of it simply by a glance.  
So, the higher-order function abstracts the rule of computing.
```python
>>> map(str, [1, 2, 3])
['1', '2', '3']
```
Simply all in one line.


#### then comes `reduce()`
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

For example:
```python
>>> def add(x, y):
... return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25
```

Of course you can use the built-in function `sum()` directly, there is no need to use the `reduce`.
But when it comes to change the list [1, 3, 5, 7, 9] to the integer 13579, reduce may be the best choice.
```python
>>> def fn(x, y):
...     return x * 10 + y 
...
>>> reduce(fn, [1, 2, 5, 7, 9])
```

Though this example is not useful, consider that `str` is a sequence, change the code above a little bit, and with `map()`, we can write function to convert `str` to `int`.
```python
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2int(c):
...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
...
>>> reduce(fn, map(char2int, '13579'))
13579
```

To sum up a `str2int` function can be:
```python
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2int(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(fn, map(char2num, s))
```
Also you can simplify these code using `lambda`.
```python
def char2num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))
```

It is, if python did not provide with a `int()` function, you absolutely can write the function yourself!  
Only takes few lines. Funny, uh-huh?
