from functools import partial, update_wrapper
import wrapt

def defer(name='_'):
    return partial(DeferDecorated, return_name=name)

class DeferDecorated():
    def __init__(self, f, return_name='_'):
        update_wrapper(self, f)
        self.underscore = wrapt.ObjectProxy(None)
        f.__globals__[return_name] = self.underscore
        self.func = f

        self.stack = []

    def defer(self, func, *args, **kwargs):
        self.stack.append((func, args, kwargs))

    def __call__(self, *args, **kwargs):
        with self:
            self.underscore.__wrapped__ = self.func(*args, **kwargs)
        return self.underscore.__wrapped__

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        while len(self.stack):
            try:
                func, args, kwargs = self.stack.pop()
                func(*args, **kwargs)
            except:
                pass
