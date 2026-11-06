#---------- comprehension 05-11-2026 ------------------------
#Extract numbers greater than 10 from a list
'''l=[5,11,15,6,8,19,20,21]
l=[num for num in l if num>10]
print(l)'''

#Convert all the string to uppercase
'''lower=['python','java','sql']
a=[s.upper() for s in lower]
print(a)'''

#extract word having more than 4 character
'''word=['cat','ballon','neon','bamboo']
length_word=[ch  for ch in word if len(ch)>=4]
print(length_word)'''

#find the multiplication of each number by 5
'''mul=[1,2,3,4,5,6]
mul_5=[num*5 for num in mul]
print(mul_5)'''

#find the vowel from the given string
'''s='prOgraMmInG'
print([ch for ch in s if ch in 'aeiouAEIOU'])'''

#remove the duplicate element from the list
'''lis=[1,3,4,6,2,2,7,1,1,6,6,8,5]
res=[]
[res.append(num) for num in lis if num not in res]
print(res)'''

#Find the common element between two lists
'''l1=[1,2,3,4]
l2=[3,4,5,6]
res=[]
common=[i for i in l1  if i in l2]
print(common)'''

#flatten a nested list
'''inp=[[1,2],[3,4],[5,6]]
#out=[1,2,3,4,5,6]
num=[j for i in inp for j in i]
print(num)'''

#-------- set comprehension ---------------------
#remove the duplicate element from a list using set comprehension
'''l=[1,2,3,2,4,1,5]
l={num for num in l}
print(l)'''

#find all numbers whose square are greater than 50
'''s={num for num in range(1,20) if num**2 > 50}
print(s)'''

#extract unique character from the string
'''s='programming'
uniq={ch for ch in s}
print(uniq)'''

#------------------ dict comprehension --------------------------
#create a dictionary of number from 1 to 10 and their square
'''d={i:i**2 for i in range(1,11)}
print(d)'''

#create a dict of number and their multiplication by 5
'''d={i:i*5 for i in range(1,11)}
print(d)'''

#create dict of even number and their square from 1 to 20
'''d={i:i**2 for i in range(1,21) if i%2==0}
print(d)'''

#convert all word in a list into uppercase and use their original word as keys
'''words=['python','java','sql']
convert={ch:ch.upper() for ch in words}
print(convert)'''

#create the dict of character and their ASCII values
'''l=['a','Y','H','i','o','p']
val={i:ord(i) for i in l}
print(val)'''

#create a dict from 2 list
'''keys=['name','age','city']
values=['hitha',21,'bangalore']
kv={i:j for i,j in zip(keys,values)}
print(kv)'''

#count the frequency of each character in a string
'''s='happiness'
count={c:s.count(c) for c in s}
print(count)'''

#count the frequency of each word in a sentence
'''s='python is easy and python is powerful'
c={c:len(c) for c in s.split(' ')}
print(c)'''

#reverse the keys and values in a dictionary
'''d={'a':1,'b':2,'c':3}
alt={j:i for i,j in d.items()}
print(alt)'''






