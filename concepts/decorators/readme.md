## decorator is just a HOC (in react)

```python
def my_decorator(func):
    def wrapper_func(*args, \*\*kwargs):
        print('Adding extra funcionality')
        func(*args, \*\*kwargs)
    return wrapper_func

@my_decorator
def hello(string, emoji=":("):
    print('Helloooo ' + string + emoji)

hello("Booyeah")
```
