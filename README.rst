|PyPI version|

Install
-------

``pip install pipe-fn``

pipe-fn
=======

Function transformation purely.

.. code:: python


    from pipe_fn import e


    # e is the identity mapping


    def add(this, other):
        return this + other


    print([1, 2, 3] | e / sum)
    # sum([1, 2, 3])
    # => 6

    print([2, 3, -1] | e ** {'key': lambda x: -x} / sorted)  # set kwargs
    # sorted([2, 3, -1], key=lambda x: -x)
    # => [3, 2, -1]

    print([[1], [2], [3]] | e / sum * ([],))  # set args
    # sum([[1], [2], [3]], [])
    # => [1, 2, 3]


    def my_func(self, *args, **kwargs):
        return self, args, kwargs


    print([1, 2, 3]
          | e
          ** dict(a=1, b=2, c=3)  # you should set kwargs first because of the high priority of `**` operator.

          * (4, 5, 6)  # it'okay to change the order of setting `args` and setting `function`.
          / my_func)
    # => ([1, 2, 3], (4, 5, 6), {'a': 1, 'b': 2, 'c': 3})


    print(1 | e / add * (1,))
    # add(1, 1)
    # => 2


    def double(x):
        return 2 * x


    # and then composition
    print(1 | (e / add * (2,) + double + double))
    # double(double(add(1, 2))
    # => 12 = (1 + 2) * 2 * 2


    # set single arg
    [['a'], ['b']] | e / sum @ [] \
                   | e / print
    # print(sum([['a'], ['b']], []))
    # => [1, 2]

    def double(x):
        return 2 * x


    [1, 2, 3] | e / std.general.Sum @ double  \
              | e / print
    # print(Sum([1,2,3], double))
    # => 12

.. |PyPI version| image:: https://img.shields.io/pypi/v/pipe-fn.svg
   :target: https://pypi.python.org/pypi/pipe-fn
