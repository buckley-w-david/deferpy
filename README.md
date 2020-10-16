# defer

Defer actions until the end of a function. Like the feature of the same name from go.

## Installation

```bash
 $ pip install deferpy
```

## Usage

```python
>>> from deferpy import defer
>>> @defer
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
>>> @defer
... def func():
...     func.defer(print, "!")
...     func.defer(print, "World", end="")
...     func.defer(print, "Hello,", end=" ")
... 
>>> func()
Hello, World!
>>>
```
