l=[4,3,2,48,123,46]
l.sort()
l
[2, 3, 4, 46, 48, 123]

l.sort(l)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l.sort(l)
TypeError: sort() takes no positional arguments

l
[2, 3, 4, 46, 48, 123]
l.sort(reverse=True)
l
[123, 48, 46, 4, 3, 2]

l=[156,23,56,3,2,08,7]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

l=[156,23,56,3,2,8,7]
l.reverse()
l
[7, 8, 2, 3, 56, 23, 156]


l=['hello','good','bye','great','honesty','loyalty']
sorted(l)
['bye', 'good', 'great', 'hello', 'honesty', 'loyalty']

s=sorted(l)
s
['bye', 'good', 'great', 'hello', 'honesty', 'loyalty']

s=sorted(l,reverse=True)
s
['loyalty', 'honesty', 'hello', 'great', 'good', 'bye']
l
['hello', 'good', 'bye', 'great', 'honesty', 'loyalty']
s
['loyalty', 'honesty', 'hello', 'great', 'good', 'bye']

reversed(s)
<list_reverseiterator object at 0x00000256CDBDF400>
list(reversed(s))
['bye', 'good', 'great', 'hello', 'honesty', 'loyalty']
str(reversed(s))
'<list_reverseiterator object at 0x00000256CDBDFC10>'
str(list(reversed(s)))
"['bye', 'good', 'great', 'hello', 'honesty', 'loyalty']"
s
['loyalty', 'honesty', 'hello', 'great', 'good', 'bye']
' '.join(s)
'loyalty honesty hello great good bye'
reversed(s)
<list_reverseiterator object at 0x00000256CDBDFD90>
str(reversed(s))
'<list_reverseiterator object at 0x00000256CDBDF610>'
list(reversed(s))
['bye', 'good', 'great', 'hello', 'honesty', 'loyalty']

' '.join(sorted(s))
'bye good great hello honesty loyalty'
' '.join(sorted(s,reverse=True))
'loyalty honesty hello great good bye'


l=['mango','apple','papaya','jackfruit','grapes','pineapple']
min(l)
'apple'
l=['mango','apple','papaya','jackfruit','grapes','pineapple']
max(l)
'pineapple'
min(l,key=len)
'mango'
l=['apple','mango','papaya','jackfruit','grapes','pineapple']
min(l,key=len)
'apple'
l=['apple','mango','papaya','ani','jackfruit','grapes','pineapple']
min(l,key=len)
'ani'
max(l,key=len)
'jackfruit'
l=['apple','mango','papaya','ani','grapes','pineapple','pear']
max(l,key=len)
'pineapple'





