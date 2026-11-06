#---------BREAK STATEMENT-----------------
'''for i in range(1,11):
    if i==5 and i==10:
        break
    else:
        print(i)'''

'''i=1
while i<=10:
    if i%2==0:
        break
    print(i)
    i+=1'''

for i in range(1,100):
    break
    print(i)

#prime no
'''n=int(input('enter the number:'))
c=0
for i in range (2,n):
    c+=1
    if n%i==0:
        print('not the prime')
        print('iterations:',c)
        break
else:
        print('prime number')
        print('iterations:',c)'''

 
# more efficent prime no
'''n=int(input('enter:'))
c=0
for i in range(2,int(n**0.5)+1):
    c+=1
    if n%i==0:
        print('not prime')
        print('iterations:',c)
        break;
else:
     print('prime number')
     print('iterations:',c)'''
     
#wap to find the first non repeating char of a string
'''s=input('enter the string:')
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break
else:
    print('there is no nom repeating character')'''

#wap to check whether the str contains only lower or not
'''s=input('enter:')
for ch in s:
    if not('a'<=ch<='z'):
        print('string contains other than only lowercase chars')
        break
else:
    print('string contains only lowercase')'''

    
#wap to check whether the tuple is homogeneous or not
'''t=eval(input('enter the numbers:'))
a=type(t[0])
for i in t:
    if type(i)!=a:
        print('not homogeneous')
        break
else:
    print('homogeneous')'''
    
#wap to find the first repeating char
'''s=input('enter the string:')
for i in range (len(s)):
    if s[i] in s[:i]:
        print('first repeated character',s[i])
        break'''


##---------------infinite loop-----------------------
#guess the number
import random
stored=random.randint(30,300)
##stored=150
while True:
    num=int(input('enter the number:'))
    if num==stored:
        print('correct guess')
        break
    elif num>stored:
        print('give the lesser number')
    else:
        if num<stored:
         print('give the greater number')
        
