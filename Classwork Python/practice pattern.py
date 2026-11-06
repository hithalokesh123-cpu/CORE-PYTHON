'''def rev():
    s=input('enter:')
    rev=' '
    for i in s:
        rev=i+rev
    print(rev)
rev()'''

'''def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    print(fact)
factorial(5)'''

'''def is_prime():
    n=int(input('enter the number:'))
    for i in range (2,n):
        if n%i==0:
            return f'{n} is not prime number'
    return f'{n} is prime number'
print(is_prime())'''

#--------------FOR PRACTICE-----------------------------
'''l=['hii',45,37,'bye',14.6,78,90,'good']
out=[]
for i in l:
    if type(i)==int:
        out.append(i)
print(out)'''
        
'''t=(11,21,31,41,51,61,71,81,91,100)
length=0
for i in t:
    length+=1
print(length)'''

'''l=[1,2,3,4,5,6,7,8,9,10]
out=[]
for i in l:
    if i%2==0:
        out.append(i)
print(out)'''

'''l=[1,2,1,4,7,4,8,6,9,5,8,4,3,7,8,6]
out=[]
for i in l:
    if i not in out:
        out.append(i)
print(out)'''

'''s=input('enter the string:')
rev=' '
for i in s:
    rev=i+rev
print(rev)'''

#assignment function
#wap to check whether the number is strong or not
'''def is_strong(n):
    temp=0
    sum=0
    while  n>0:
        d=n%10
        fact =1
        for i in range(1,d+1):
            fact=fact*d
        n//10=0
    if temp==sum:'''

'''n=5
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)'''

'''def factorial(n,fact=1,i=1):
    if i==n:
        print(f'({n},{i},{fact})')
        return fact*i
    fact=fact*i
    print(f'({n},{i},{fact})')
    return factorial(n,fact,i=i+1)
print(factorial(5))'''




'''def is_perfect(n):
    sum=0
    for i in range (1,n):
       if n%i==0:
          sum=sum+i
    return sum == n
print(is_perfect(6))'''

'''def is_strong(n):
    sum=0
    i=0
    while n>0:
        d=i%10
        fact=1
        for i in range(1,n):
            fact=fact*i
            sum=sum+fact
    return sum == n
print(is_strong(14))'''


'''n=int(input('enter:'))
if n>100 and n<999:
      print('there are 3 digit number')'''

n=145
if n%10==5:
    print('the last digit is 5')

    
        


