#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any


def logged(func):
    """Wypisz przed wywołaniem funkcji jej argumenty, a po wywołaniu -
     - zwróconą wartość.
    """

    def wrapper(*args, **kwargs):
        print('you called {f.__name__}...'.format(f=func))

        # print('you called {.__name__}({}{}{})'.format(
        #     func,
        #     str(list(args))[1:-1],  # cast to list is because tuple of length one has an extra comma
        #     ', ' if kwargs else '',
        #     ', '.join('{}={}'.format(*pair) for pair in kwargs.items()),
        # ))
        val = func(*args, **kwargs)
        print('...it returned', val)
        return val

    return wrapper


@logged
def foo(*args: Any) -> int:
    return len(args)


foo(1, 2, 3)
