#!/usr/bin/env python3

# --------
# Dicts.py
# --------

print("Dicts.py")

d = {2 : "ghi", 3.45 : 3, "abc" : 6.78, 2 : "def"}
assert type(d) ==     dict
assert len(d)  ==     3
assert d       is not {2 : "def", 3.45 : 3, "abc" : 6.78}
assert d       ==     {2 : "def", 3.45 : 3, "abc" : 6.78}
assert d       ==     {2 : "def", "abc" : 6.78, 3.45 : 3}

d = dict(((2, "ghi"), (3.45, 3), ("abc", 6.78), (2, "def")))
assert type(d) ==     dict
assert len(d)  ==     3
assert d       is not {2 : "def", 3.45 : 3, "abc" : 6.78}
assert d       ==     {2 : "def", 3.45 : 3, "abc" : 6.78}
assert d       ==     {2 : "def", "abc" : 6.78, 3.45 : 3}

d = dict([[2, "ghi"], [3.45, 3], ["abc", 6.78], [2, "def"]])
assert type(d) ==     dict
assert len(d)  ==     3
assert d       is not {2 : "def", 3.45 : 3, "abc" : 6.78}
assert d       ==     {2 : "def", 3.45 : 3, "abc" : 6.78}
assert d       ==     {2 : "def", "abc" : 6.78, 3.45 : 3}

{} is not {}
{} ==     {}

d = {}
try :
    assert d[2] == None
    assert False
except KeyError as e:
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == (2,)
d[2]     = "ghi"
d[3.45]  = 3
d["abc"] = 6.78
d[2]     = "def"
assert d == {2 : "def", 3.45 : 3, "abc" : 6.78}
v = d.pop("abc")
assert v == 6.78
assert d == {2 : "def", 3.45 : 3}
try :
    d.pop("abc")
    assert False
except KeyError as e:
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == ("abc",)

d = {2 : "abc", 3 : "def", 4 : "ghi"}
assert set(d.keys())   == {2, 3, 4}
assert set(d.values()) == {"abc", "def", "ghi"}
assert set(d.items())  == {(2, "abc"), (3, "def"), (4, "ghi")}

d = {2 : "abc", 3 : "def", 4 : "ghi"}
assert 3     in d
assert 5 not in d

d = {2 : "abc", 3 : None, 4 : "ghi"}
assert d.get(3) == None
assert d.get(5) == None

d = {2 : "abc", 3 : "def", 4 : "ghi"}
e = d.copy()
assert d is not e
assert d ==     e

t = ("a", "b", "c")
u = (2, 3, 4)
z = zip(t, u)
d = dict(z)
assert d == {'a' : 2, 'b' : 3, 'c' : 4}

t = ("a", "b", "c")
u = (2, 3)
z = zip(t, u)
d = dict(z)
assert d == {'a' : 2, 'b' : 3}

t = ("a", "b", "c")
u = (2, 3, 4)
v = (5, 6)
z = zip(t, u, v)
#d = dict(z)     # ValueError: dictionary update sequence element #0 has length 3; 2 is required

assert False is not 0
assert False ==     0
assert True  is not 1
assert True  ==     1
assert 2     is not 2.0
assert 2     ==     2.0
d = {False : "abc", 0 : "def", True : "ghi", 1 : "jkl", 2 : "mno", 2.0 : "pqr"}
assert d == {False : 'def', True : 'jkl', 2  : 'pqr'}
assert d == {0     : 'def', 1    : 'jkl', 2.0 : 'pqr'}

d  = {"abc"             : "abc", "def"             : "def"}
d  = {(2, 3)            : "abc", (4, 5)            : "def"}
d  = {frozenset([2, 3]) : "abc", frozenset([4, 5]) : "def"}

#d = {{2, 3} : "abc", {4, 5} : "def"} # TypeError: set objects are unhashable
#d = {[2, 3] : "abc", [4, 5] : "def"} # TypeError: list objects are unhashable

class A :
    pass

d  = {A() : "abc", A() : "def"}
assert len(d) == 2

print("Done.")
