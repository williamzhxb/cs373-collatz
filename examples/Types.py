#!/usr/bin/env python3

#pylint: disable = function-redefined, redefined-outer-name, too-few-public-methods

# --------
# Types.py
# --------

from types import FunctionType

print("Types.py")

b = True
b = False
assert isinstance(b,    bool)
assert isinstance(bool, type)
assert issubclass(bool, bool)
assert issubclass(bool, object)

i = 2
assert isinstance(i,   int)
assert isinstance(int, type)
assert issubclass(int, int)
assert issubclass(int, object)

assert issubclass(bool, int)

f = 2.3
assert isinstance(f,     float)
assert isinstance(float, type)
assert issubclass(float, float)
assert issubclass(float, object)

c = 2 + 3j
c = complex(2, 3)
assert isinstance(c,       complex)
assert isinstance(complex, type)
assert issubclass(complex, complex)
assert issubclass(complex, object)

s = 'abc'
s = "abc"
s = str(["a", "b", "c"])
assert isinstance(s,   str)
assert isinstance(str, type)
assert issubclass(str, str)
assert issubclass(str, object)

l = [2, "abc", 3.45]
l = list((2, "abc", 3.45))
assert isinstance(l,    list)
assert isinstance(list, type)
assert issubclass(list, list)
assert issubclass(list, object)

t = (2, "abc", 3.45)
t = tuple([2, "abc", 3.45])
assert isinstance(t,     tuple)
assert isinstance(tuple, type)
assert issubclass(tuple, tuple)
assert issubclass(tuple, object)

u = {2, "abc", 3.45}
u = set([2, "abc", 3.45])
assert isinstance(u,   set)
assert isinstance(set, type)
assert issubclass(set, set)
assert issubclass(set, object)

w = frozenset([2, "abc", 3.45])
assert isinstance(w,         frozenset)
assert isinstance(frozenset, type)
assert issubclass(frozenset, frozenset)
assert issubclass(frozenset, object)

d = {2: "def", 3.45: 3, "abc": 6.78}
d = dict([(2, "def"), (3.45, 3), ("abc", 6.78)])
assert isinstance(d,    dict)
assert isinstance(dict, type)
assert issubclass(dict, dict)
assert issubclass(dict, object)

def f (v) :
    return v + 1
assert isinstance(f,            FunctionType)
assert isinstance(FunctionType, type)
assert issubclass(FunctionType, FunctionType)
assert issubclass(FunctionType, object)

class A :
    def __init__ (self, i, f) :
        pass

x = A(2, 3.45)
assert isinstance(x, A)
assert isinstance(A, type)
assert issubclass(A, A)
assert issubclass(A, object)

assert isinstance(type, type)
assert issubclass(type, type)
assert issubclass(type, object)

print("Done.")
