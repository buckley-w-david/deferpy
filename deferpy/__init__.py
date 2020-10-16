from functools import partial, update_wrapper

class defer():
    def __init__(self, f):
        update_wrapper(self, f)
        self.func = f

        self.stack = []

    def defer(self, func, *args, **kwargs):
        self.stack.append(partial(func, *args, **kwargs))

    def __call__(self, *args, **kwargs):
        with self:
            return self.func(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        while len(self.stack):
            try:
                self.stack.pop()()
            except:
                pass
