Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
>>> type(a)
<class 'int'>
>>> b=7.8
>>> type(b)
<class 'float'>
>>> c="python"
>>> type(c)
<class 'str'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=2j+8
>>> type(g)
<class 'complex'>
>>> i=7j
>>> type(i)
<class 'complex'>
>>> k=9i
SyntaxError: invalid decimal literal
>>> l=j
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l=j
NameError: name 'j' is not defined
>>> m="j"
>>> type(m)
<class 'str'>
>>> x=True
>>> type(x)
<class 'bool'>
>>> z=true
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    z=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(z)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    type(z)
NameError: name 'z' is not defined
>>> z="True"
>>> type(z)
<class 'str'>
