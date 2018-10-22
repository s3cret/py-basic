### Higher-Order Function
-------------------------

#### Variable can point to Function

As for python built-in function`abs()`:
```python
>>> abs(-10)
10
```
What if just `abs`

```python
>>> abs
<built-in function abs>
```

>So you can see that `abs(-10)` is the function-call, and the `abs` is the funciton itself.

We can assign the return value to a variable.
```python
>>> x = abs(-10)
>>> x
10
```

What if we assign the function itself to a variable?

```python
>>> f = abs
>>> f
<built-in function abs>
```

#### Conclusion: Function itself can assign to a variable & A variable can point to a function.
```python
>>> f = abs
>>> f(-10)
10
```

> It indicated that f is already pointed to the `abs` function itself.

#### Function name itself is also variable.
What if a function name points to another object?

```python
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

After you manupulate `abs` point to 10, you cannot call the original function.  
Because the variable `abc` has no longer pointed to the original function.  
> You absolutely should not write such code; In this case, it is just written to show a truth that function name itself is actually a variable.  
To recover the `abs` function, please restart your python environment.


As a matter of fact, the `abs` function is defined in the `__builtin__` module, so if you want to change it globally, do it with the prefix `__builtin__` as `__builin__.abs = 10`.

#### Passing Function (just like variable)
Now that a variable can point to a function, also a function can receive variables,  
then a function can receive another function as variable.

The simplest example:
```python
def add(x, y, f):
    return f(x) + f(y)
```
When we call `add(-5, 6, abs)`, parameter `x`, `y`, `f` receive `-5`, `6` and `abs` respectively.  
According to the definition of function, we can understand the above function.

```php
x <== -5
y <== 6
f <== abs
f(x) + f(y) = abs(-5) + abs(6) = 11
```

#### In short
At last, pass the function as a variable(parameter) is the so-called higher-order function.  
This is what the Functional Programming do with the high-abstract paradigm.
