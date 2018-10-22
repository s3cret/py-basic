### slice-notation
It's pretty simple really:

```python
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
```
There is also the `step` value, which can be used with any of the above:
```python
a[start:end:step] # start through not past end, by step
```
The key point to remember is that the `:end` value represents the first value that is _not_ in the selected slice. So, the difference beween `end` and `start` is the number of elements selected (if step is 1, the default).

The other feature is that `start` or `end` may be a negative number, which means it counts from the end of the array instead of the beginning. So:
```python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
```
Similarly, `step` may be a negative number:

```python
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```
Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for `a[:-2]` and `a` only contains one element, you get an empty list instead of an error.  
 Sometimes you would prefer the error, so you have to be **aware** that this may happen.

[link to stackoverflow](https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation)
