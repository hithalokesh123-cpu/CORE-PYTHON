Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
School.sname
'Nazereth'
obj.sname
'Nazereth'
s2=School()
s2.sname
'Nazereth'
s2.princi
'Helda lobo'
obj.princi
'Helda lobo'

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
School.__dict__
mappingproxy({'__module__': '__main__', 'sname': 'Nazereth', 'loc': 'bangalore', 'princi': 'Helda lobo', '__dict__': <attribute '__dict__' of 'School' objects>, '__weakref__': <attribute '__weakref__' of 'School' objects>, '__doc__': None})
s1.__dict__
{}

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
s1.__dict__
{'name': 'Nesara', 'std': 7}
s2.__dict__
{'name': 'Hitaishree', 'std': 6}
s3.__dict__
{'name': 'jittu', 'std': 8}
a=10
type(a)
<class 'int'>
s='hello'
type(s1)
<class '__main__.School'>
type(int)
<class 'type'>
s1.std
7

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
s1.name
'Nesara'
s2.phno
9988776655
s3.std
7

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
the name is: Nesara
the std is: 5
the phno is: 9876543212
the addr is: CKM
s2.display()
the name is: Jitu
the std is: 6
the phno is: 9988776655
the addr is: Guntur
s3.display()
the name is: Jyoti
the std is: 7
the phno is: 6677889955
the addr is: Gulbarga

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
the name is: Nesara
the std is: 5
the phno is: 9876543212
the addr is: CKM
s1.ch_phno(7896543212)
s1.display()
the name is: Nesara
the std is: 5
the phno is: 7896543212
the addr is: CKM

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
the name is: Nesara
the std is: 5
the phno is: 9876543212
the addr is: CKM
s1.static()
im a helping method
School.static()
im a helping method
s1()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s1()
TypeError: 'School' object is not callable
callable(s1)
False
callable(School)
True

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
the name is: Nesara
the std is: 5
the phno is: 9876543212
the addr is: CKM
s1()
object is being called
s2()
object is being called
x=10
x()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x()
TypeError: 'int' object is not callable
int()
0

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
c1.bal
10000
c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 10000}

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
>>> c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 10000}
>>> c1.withdraw()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c1.withdraw()
AttributeError: 'Bank' object has no attribute 'withdraw'
>>> 
============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
>>> c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 10000}
>>> c1.withdraw()
enter:5000
>>> c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 5000}
>>> c1.withdraw()
enter:10000
>>> c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': -5000}
>>> 
============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
>>> c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 10000}
c1.withdraw()
enter:50000
insufficient bal
c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 10000}
c1.withdraw()
enter:650
withdraw successfull
c1.__dict__
{'name': 'Hita', 'addr': 'Banalore', 'bal': 9350}

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
c1.withdraw()
enter:70000
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c1.withdraw()
  File "C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py", line 65, in withdraw
    raise ValueError('insufficient bal')
ValueError: insufficient bal

============= RESTART: C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py =============
c1.withdraw()
enter:12000
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c1.withdraw()
  File "C:/Users/Dell/OneDrive/Desktop/PYTHON/oops.py", line 66, in withdraw
    raise InsufficientBalance ('enter lesser amount')
InsufficientBalance: enter lesser amount
NewBank.__dict__
mappingproxy({'__module__': '__main__', 'withdraw': <function NewBank.withdraw at 0x0000017EE3670C10>, '__doc__': None})
