# deferpy

```
Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed in last-in-first-out order.
```

[The Go Blog](https://blog.golang.org/defer-panic-and-recover) has a good explanation of the behavior of `defer`. This package attempts to recreate the behavior as closely as possible.

## Installation

```bash
 $ pip install deferpy
```

## Usage

Check out the `tests` to see more examples.

```python
>>> from deferpy import defer
>>> @defer()
... def function(a, b, c):
...     function.defer(print, a)
...     function.defer(print, b)
...     function.defer(print, c)
...     return a + b + c
... 
>>> print(function(1, 2, 3))
3
2
1
6
>>> @defer()
... def func():
...     for i in range(10):
...         func.defer(print, i)
... 
>>> func()
9
8
7
6
5
4
3
2
1
0
```
