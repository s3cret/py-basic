### Generator
-------------
From the list comprehension, we can generate a full list stored in the memory.  
As for a very large list, though it is generated  
`What if we just need to use few of the front index elements?`  
Then numbers of the elements are going to waste the memory.  

In this case, we can use generator to `compute the next and next element on the fly`.

#### It is so simple to generate a generator
Just use `()` instead of the list comprehension using `[]`

You can use `next()` or use `for` loop
Use `next()` may cause `StopIteration` traceback.

#### Examples
* Fibonacci
    ```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
```
And the output:
    ```python
>>> fib(6)
1
1
2
3
5
8
```

* Fibonacci with yield
```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
```
>
It is another way to define a generator.  
Once if a function contains the python reserved word `yield`,  
then it becomes a generator rather than a regular function.

For regular function, it will return when program counter point to the `return` line or the pc goes to the end of the function.  
As for the generator function, it executes and computes the next element and return when it sees the reserved word `yield`. Next time you call `next()`, it will continue to the last-exit yield line and execute the following lines. Pretty nice, huh?

Again, we usually use `for` loop to manupulate the generator, of course you can use `next()`, too.

`Compute the next and next element on the fly!`
