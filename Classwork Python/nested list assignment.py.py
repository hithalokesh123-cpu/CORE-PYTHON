Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[10,20,30]
len(l)
3
type(l)
<class 'list'>

'''homogeneous collection'''
'homogeneous collection'
l=['ammu','roopa','king','rana']
len(l)
4
l[2]
'king'
l[2]='raj'
l
['ammu', 'roopa', 'raj', 'rana']
l[1][2]=p
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l[1][2]=p
NameError: name 'p' is not defined
l[1][2]
'o'


'heterogenous collection'
l=[50.6,'good',10,8j,'h',3.3]
len(l)
6
l[1]
'good'


'Nested list'
l=[500,450,[100,'beautiful'],5.99],['hi',14.5,8j,9],[5j,10,'root',12.6]

len[l]
3
>>> l[1]
['hi', 14.5, 8j, 9]

>>> l[2]
[5j, 10, 'root', 12.6]

>>> l[0][2][1]
'beautiful'

>>> l[0][3]=6.0
>>> l[0][3]
6.0

>>> l[2][0]
5j

>>> l[2][2]='leaf'

>>> l[2]
[5j, 10, 'leaf', 12.6]

>>> [5j, 10, 'leaf', 12.6]

>>> l
([500, 450, [100, 'beautiful'], 6.0], ['hi', 14.5, 8j, 9], [5j, 10, 'leaf', 12.6])

>>>'''id reference address access'''
>>>l=[10,20,30]
>>>id(l)
1136570913280

>>>id(l[0])
1136560505360
