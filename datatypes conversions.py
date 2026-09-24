Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#integers
int(8)
8
int(6.7)
6
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


==================================================================================== RESTART: Shell ====================================================================================
#string
str("venkat")
'venkat'
str(0.7)
'0.7'
str(8+9j)
'(8+9j)'
str("true")
'true'
str(""True")
    
SyntaxError: unterminated string literal (detected at line 1)
str("00")
    
'00'

==================================================================================== RESTART: Shell ====================================================================================
#float
    
float(0.7)
...     
0.7
>>> float(8+9j)
...     
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float(8+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
...     
1.0
>>> float(False)
...     
0.0
>>> 
==================================================================================== RESTART: Shell ====================================================================================
>>> #complex
...     
>>> complex(8+9j)
...     
(8+9j)
>>> complex("venkat")
...     
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex("venkat")
ValueError: complex() arg is a malformed string
>>> 
==================================================================================== RESTART: Shell ====================================================================================
>>> #boolean
...     
>>> bool(True)
...     
True
>>> bool(False)
...     
False
>>> bool("venkat")
...     
True
>>> bool(0.0)
...     
False
>>> bool(8+9j)
...     
True
