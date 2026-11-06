Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''LIST APPEND'''
'LIST APPEND'
n=[10,200,420,'hello',20]
n.append('ran')
n
[10, 200, 420, 'hello', 20, 'ran']

# pass collection
n.append[3,'room',70]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    n.append[3,'room',70]
TypeError: 'builtin_function_or_method' object is not subscriptable
n.append([3,'room',70])
n
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 70]]
n.append()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    n.append()
TypeError: list.append() takes exactly one argument (0 given)

# list.insert()function
n.insert(10,98)
n
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 70], 98]
n.insert(6[2],40)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    n.insert(6[2],40)
TypeError: 'int' object is not subscriptable
n[6].insert(2,40)
n
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 40, 70], 98]

#list.extend([v1,v2....vn])
n.extend(['hi',220,4.5])
n
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 40, 70], 98, 'hi', 220, 4.5]

n.extend('geetha')
n
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 40, 70], 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h', 'a']
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 40, 70], 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h', 'a']
[10, 200, 420, 'hello', 20, 'ran', [3, 'room', 40, 70], 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h', 'a']



#LIST REMOVE FUNCTION

#POP(),POP(INDEX)
N.POP()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    N.POP()
NameError: name 'N' is not defined. Did you mean: 'n'?
n.pop()
'a'
n.pop(6)
[3, 'room', 40, 70]
n.pop('hello')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    n.pop('hello')
TypeError: 'str' object cannot be interpreted as an integer

#remove()
n.remove('ran')
n
[10, 200, 420, 'hello', 20, 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h']
[10, 200, 420, 'hello', 20, 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h']
[10, 200, 420, 'hello', 20, 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h']



n.remove(25)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    n.remove(25)
ValueError: list.remove(x): x not in list


#clear()
n.clear()
n
[]


#delect the entire list along with the variable
del.n
SyntaxError: invalid syntax
>>> del n
>>> n
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> NameError: name 'n' is not defined
SyntaxError: invalid syntax
>>> 
>>> n=[10, 200, 420, 'hello', 20, 98, 'hi', 220, 4.5, 'g', 'e', 'e', 't', 'h']
>>> n.remove('e')
>>> n
[10, 200, 420, 'hello', 20, 98, 'hi', 220, 4.5, 'g', 'e', 't', 'h']
>>> 
>>> 
>>> #nested list
>>> m=['riya',110,20.5,['hi',2.5],'joo',[35,75,26],'doms']
>>> m.remove(0)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    m.remove(0)
ValueError: list.remove(x): x not in list
>>> m.remove('riya')
>>> m
[110, 20.5, ['hi', 2.5], 'joo', [35, 75, 26], 'doms']
>>> m[4][1].remove(75)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    m[4][1].remove(75)
AttributeError: 'int' object has no attribute 'remove'
>>> m[4][1].pop()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    m[4][1].pop()
AttributeError: 'int' object has no attribute 'pop'
>>> AttributeError: 'int' object has no attribute 'pop'
SyntaxError: invalid syntax
>>> m[4].remove(75)
>>> m
[110, 20.5, ['hi', 2.5], 'joo', [35, 26], 'doms']
