from functools import reduce, update_wrapper


def pipe_call(a, b):
    return b(a)


def and_then(*f):
    def and_then_call(x):
        return reduce(pipe_call, f, x)

    return and_then_call


class Pipe:
    def __init__(self, f, args, kwargs, f_continue: tuple = None):
        self.f = f
        self.f_continue = f_continue
        self.args = args
        self.kwargs = kwargs
        update_wrapper(self, f)

    def __truediv__(self, other):
        return Pipe(other, self.args, self.kwargs)

    def __pow__(self, kwargs):
        kwargs.update(self.kwargs)
        return Pipe(self.f, self.args, kwargs)

    def __mul__(self, args):
        if not isinstance(args, tuple):
            args = tuple(args)
        return Pipe(self.f, self.args + args, self.kwargs)

    def __call__(self, left):
        if not self.f_continue:
            return self.f(left, *self.args, **self.kwargs)
        else:
            return reduce(pipe_call,
                          self.f_continue,
                          self.f(left, *self.args, **self.kwargs))

    def __matmul__(self, other):
        return Pipe(self.f, self.args + (other, ), self.kwargs)

    def __ror__(self, left):
        return self(left)

    def __add__(self, then):
        if not callable(then):
            raise ValueError(f'`callable` expected, but get a `{then.__class__}` instead.')
        if not self.f_continue:
            return Pipe(self.f, self.args, self.kwargs, (then,))
        else:
            return Pipe(self.f, self.args, self.kwargs, self.f_continue + (then,))


e = Pipe(lambda x: x, (), dict())
