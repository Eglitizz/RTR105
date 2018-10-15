Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> eee="cau"+"tu"
>>> eee = eee+1

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    eee = eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> print(eee)
cautu
>>> type(eee)
<type 'str'>
>>> type(cau)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(cau)
NameError: name 'cau' is not defined
>>> type(1)
<type 'int'>
>>> pritnt(float(99)+11)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pritnt(float(99)+11)
NameError: name 'pritnt' is not defined
>>> print(float(99)+100)
199.0
>>> print(10/5)
2
>>> 
