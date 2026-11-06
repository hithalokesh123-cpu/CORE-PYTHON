#FUNCTIONS
#1.WITHOUT ARGS AND WITHOUT RETURENS
'''def sum():
    n1=int(input('enter the number1:'))
    n2=int(input('enter the number2:'))
    print(n1+n2)
sum()'''
    
#wap to reverse a string without slicing
'''def rev():
    s=input('enter:')
    rev=''
    for i in s:
        rev=i+rev
    print(rev)
rev()  '''      


#using reversed() and join()  
'''def rev():
    s=input('enter:')
    rev=''.join(list(reversed(s)))
    print(rev)
rev()'''

#using slicing 
'''def rev():
    s=input('enter:')
    rev=s[::-1]
    print(rev)
rev()'''

#2.WITH ARG WITHOUT RETURN
'''def add(n1,n2):
    print(n1+n2)
add(31,41)'''

#wap to find factorial of a number
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(5)'''

#using while
'''def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    print(fact)
factorial(5)'''

#3.WITHOUT ARG WITH RETURN
'''def sam():
    n1=int(input('enter the number1:'))
    n2=int(input('enter the number2:'))
    return n1+n2
print(sam())'''

#wap to check whether the number prime or not
'''def is_prime():
    n=int(input('enter:'))
    for i in range(2,n):
        if n%i==0:
            return f'{n} is not prime number'
    return  f'{n} is prime number' 
print(is_prime())'''

#WITH ARGS WITH RETUEN
'''def sum(a,b):
    return a+b
print(sum(10,20))'''

#wap to remove duplicates from a list
'''def remove_dup(l):
    out=[]
    for i in l:
        if i not in out:
             out.append(i)
    return out
print(remove_dup([1,5,2,2,5,6,4,5,5]))'''
'''print(remove_dup(eval(input("enter:"))))'''

#wap to check whether the number is perfect number or not    (6,28) factor sum
'''def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==n
print(is_perfect()) '''       
    
#wap to check whether the number is strong number           fact and sum  (,1,2145,40585)
'''def is_strong(n):
    sum=0
    temp=n
    while n>0:
        d=n%10
        fact=1
        for i in range(1,d+1):
            fact*=i
        sum+=fact
        n=n//10
    return(is_strong(145))'''
    

    
#using for loop
'''def is_strong(n):
    sum=0
    for d in str(n):
        fact=1
        for i in range(1,int(d)+1):
            fact*=i
        sum+=fact
    return sum==n
print(is_strong(40585))'''
    
#using NESTED FUNCTON
'''def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return(fact)

def is_strong(n):
    sum=0
    for d in str(n):
        sum+=factorial(int(d))
    return sum==n
print(is_strong(145))'''

 #USING NESTED FUNCTION    
#wap to print the strong number between 1 to 10000
'''def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return(fact)

def is_strong(n):
    sum=0
    for d in str(n):
        sum+=factorial(int(d))
    return sum==n


def is_strong3():
    for i in range(1,10001):
        if is_strong(i):
            print(i)'''

#USING NESTED FUNCTION            
#wap to print the prime number between 1 to 1000
'''def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return f'{n} is not prime number'
    return  f'{n} is prime number'


def prime_numbers():
    for i in range(1,1001):
        if is_prime(i):
           print(i)
print(prime_numbers())'''

#USING NESTED FUNCTION
#wap to print the perfect number between 1 to 1000        (6, 28, 496)
'''def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==n
      
    
def perfect_numbers():
    for i in range(1,1001):
        if is_perfect(i):
           print(i)
print(perfect_numbers())'''

#USING NESTED FUNCTION
#wap to print the arm strong number between 1 to 1000
def arm_strong(n):
   temp=n
   sum=0
   l=len(str(n))
   while n>0:
     d=n%10
     sum+=d**l
     n//=10
   if sum==temp:
       return( "is arm strong number")

def arm_strong_numbers():
    for i in range(1,1001):
        if arm_strong(i):
           print(i)
print(arm_strong_numbers())    
# output 1 2 3 4 5 6 7 8 9 153 370 371 407 None

