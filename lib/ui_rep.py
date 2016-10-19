#!/bin/python2
from inspect import getdoc, getargspec
from collections import namedtuple


UI_Func = namedtuple('ui_func', ['name', 'desc', 'args', 'func'], verbose=False)

Func_Arg = namedtuple('func_args', ['name', 'desc', 'pos_vals'], verbose=False)

def ui_from_func(func, args):
    desc = getdoc(func)
    name = func.__name__
    args1, _, kwargs, _ = getargspec(func)
    # +1 accounts for self
    if (len(args) + 1 < len(args1)):
        raise Exception("Not enough args passed to %s" % name)
    return UI_Func(name, desc, args, func)

