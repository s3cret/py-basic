### Python __builtins__.sorted()
#### sorted()
* If `x < y`, then return -1;
* If `x == y`, then return 0;
* If `x > y`, then return 1;
#### Just look
```python
>>> sorted([36, 5, 12, 9, 21])
[5, 9, 12, 21, 36]
```

#### `sorted()` is also a higher-order function
So it can receive a function as its parameter

**Example:**
Customize reverse func
```python
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
```

Call it:
```python
>>> sorted([36, 5, 12, 9, 21], reversed_cmp)
[36, 21, 12, 9, 5]
```

But the `sorted()` function itself already contains the option `reverse`:
```python
>>> sorted([36, 5, 12, 9, 21], reverse=True)
[36, 21, 12, 9, 5]
```
