Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=3;b=7
@=9
SyntaxError: invalid syntax
$=10
SyntaxError: invalid syntax
_=40
print(_)
40
_a=100
print(+a)
3
_a=100
print(_a)
100
if=20
SyntaxError: invalid syntax
while=6
SyntaxError: invalid syntax
a=2,3,4,5,6,7,8,9
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c=3,4,5
print(a,b,c)
3 4 5
a,b,c,=4,5,6,7,8,9,10
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a,b,c,=4,5,6,7,8,9,10
ValueError: too many values to unpack (expected 3, got 7)
first name="pooja"
SyntaxError: invalid syntax
fist_name="pooja"
print(first_name)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(first_name)
NameError: name 'first_name' is not defined. Did you mean: 'fist_name'?
first_name="pooja"
print(first_name)
pooja
a=(1,2,3)
print(a)
(1, 2, 3)
a.b.c=(5,6,7)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.b.c=(5,6,7)
AttributeError: 'tuple' object has no attribute 'b'
print(a,b,c)
(1, 2, 3) 4 5
>>> a=90
>>> print(a)
90
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
>>> name="pooja"
>>> print(name)
pooja
>>> Name="pooja"
>>> print(Name)
pooja
>>> NAME="POOJA"
>>> PRINT("NAME")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    PRINT("NAME")
NameError: name 'PRINT' is not defined
>>> NAME="POOJA"
>>> PRINT(NAME)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    PRINT(NAME)
NameError: name 'PRINT' is not defined
>>> NAME="POOJA"
>>> print(NAME)
POOJA
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print
<built-in function print>
>>> (
... print(a,b,c)
... print(a,b,c)
SyntaxError: '(' was never closed
>>> (
...     print(a,b,c)
... (
... print(a,b,c)
