from typing import Callable


def function(hook: Callable, hook_args: tuple) -> None:
    hook(*hook_args)


def func(x, y):
    x.append(y)


x = []
y = 1
function(func, (x, y))
function(func, (x, y))
print(x)