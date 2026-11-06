#TYPES OF ARGUMENTS
#-----------------POSITIONAL ARGUMENT-----------------------
'''def positional(name,addr,phno,marks):
    print('Name is:',name)
    print('Address  is:',addr)
    print('Phnoo is:',phno)
    print('Marks is:',marks)
positional('hitha','madavara',4567788999,98)'''

#output
##Name is: hitha
##Address  is: madavara
##Phnoo is: 4567788999
##Marks is: 98



#ORDER MATTERS
'''def positional(name,addr,phno,marks):
    print('Name is:',name)
    print('Address  is:',addr)
    print('Phnoo is:',phno)
    print('Marks is:',marks)
positional('madavara',4567788999,'hitha',98)'''

#output
##Name is: madavara
##Address  is: 4567788999
##Phnoo is: hitha
##Marks is: 98


#PAR==VAL
'''def positional(name,addr,phno,marks):
    print('Name is:',name)
    print('Address  is:',addr)
    print('Phnoo is:',phno)
    print('Marks is:',marks)
positional('madavara',4567788999,98)'''
#ERROR MSG THE 1 ARG IS MISSING


#-----------------DEFAULT ARGUMENTS--------------------------
'''def default(name,addr,phno1,phno2=None):
    print('Name is:',name)
    print('Address  is:',addr)
    print('Phnoo1 is:',phno1)
    print('Phnoo2 is:',phno2)
default('hitha','nelmangala',45678987654)'''

#output
##Name is: hitha
##Address  is: nelmangala
##Phnoo1 is: 45678987654
##Phnoo2 is: None


#---------------KEYWORD ARGUMENT--------------------------------
'''def keyword(name,addr,phno1,phno2):
    print('Name is:',name)
    print('Address  is:',addr)
    print('Phnoo1 is:',phno1)
    print('Phnoo2 is:',phno2)
keyword(phno1='None',addr='bangalore',name='asha',phno2=2356784560) '''  

#output
##Name is: asha
##Address  is: bangalore
##Phnoo1 is: None
##Phnoo2 is: 2356784560

#--------------------variable-length argumnent-------------------------
#--------------------*args---------------------------------------
'''def sample1(*args):
    print(args)
sample1(1,3,4,6,7,8,0,12,5)'''
#1, 3, 4, 6, 7, 8, 0, 12, 5)

#-------------------------**kwargs--------------------------------
'''def sample2(**kwargs):
    print(kwargs)
sample2(a=13,b=15,c=14,d=31)'''
#{'a': 13, 'b': 15, 'c': 14, 'd': 31}

#---------------------UNPACKING CONCEPT---------------------------------
'''l=[1,2,3,4,5]
def sam(a,b,c,d,e):
    print(a+b+c+d+e)
sam(*l)'''

#---------------------SCOPE OF VARIABLE---------------------------------
#LOCAL ---> GLOBAL( no MODIFICATION)
'''a=50
b=100
print('outside the function before modification:',a,b)
def scope():
    global a,x,y
    a=500
    x=70
    y=80
    print('inside  the function before modification:',a,b,x,y)
scope()
print('outside the function before modification:',a,b,x,y)'''

#LOCAL ---->NESTED FUNCTION------------------
'''a=10
b=20
def outer():
    x=30
    y=40
    a=500
    print("from outer function")
    print('global:',a,b)
    print('local:',x,y)
    def inner():
        nonlocal x
        m=100
        n=200
        x=400
        print("from inner function")
        print('global:',a,b)
        print('local:',m,n)
        print('enclosing:',x,y)
    inner()
    print('local after modification:',x,y)
outer()'''    


#----------------RECURSION FUNCTION-------------------------------
'''l=[1,2,[4,5,(9,8,{12,34,(9,11,17),35},12,18),19,89],66,1,5]
def sum_int(l):
    sum=0
    for i in l:
        if type(i)==int:
            sum+=i
        elif type(i) in [list,tuple,set]:
            sum+=sum_int(i)
    return sum
print(sum_int(l))'''
            
#---------FACTORIAL------------
'''def fact(n):
    if n==1 or n==0:
        return 1
    
    return n*fact(n-1)
print(fact(5))'''

#sum of natural number
'''def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)
print(sum_natural(5))'''


#sum of whole number
'''def sum_whole(n):
    if n==0:
        return 0
    return n+sum_whole(n-1)
print(sum_whole(5))'''

#output 1 2 3 4 5 4 3 2 1
'''def sample(n,i=1):
    print(i,end=' ')
    if i==n:
        return
    sample(n ,i=i+1)
    print(i,end=' ')
sample(5)'''

#wap to fibonacci series
#for loop
'''n=int(input('enter the number:'))
a=0
b=1

for i in range(n):
    print(a,end='')

    c=a+b
    a=b
    b=c'''

#while loop
'''a=0
b=1
i=0
while i<n:
    print(a,end='')

    c=a+b
    a=b
    b=c
    i+=1'''


#recursion
'''def fibonacci(n,a=0,b=1,i=0):
    if i>=n:
        return 
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    return fibonacci(n,a,b,i=i+1)
fibonacci(5)'''



#--------USING WHILE LOOP IN RECURSION----------
#reversed the string

'''s="abc"
rev=''
i=0
while i<len(s):
    rev=s[i]+rev
    i+=1
print(rev)'''


'''def reverse_str(s,rev='',i=0):
    if i>=len(s):
        return rev
    rev=s[i]+rev
    return reverse_str(s,rev,i=i+1)
print(reverse_str('sparsh masala'))'''


#reversed the number
'''def reverse_num(n,rev=0):
    if n<=0:
        return rev
    d=n%10
    rev=(rev*10)+d
    n=n//10
    return reverse_num(n,rev)
print(reverse_num(163))'''

#---------------problem on recursion----------------------------   
#wap to print python for 5 times
'''def prt5time(n,s,i=0):
    if i == n:
        return
    print(s)
    return prt5time(n,s,i=i+1)
prt5time(5,'python')'''

#wap to print n natural numbers
'''def natural_num(n,i=1):
    if i == n:
        return i
    print(i)
    return natural_num(n,i=i+1)
print(natural_num(6))'''

#wap to print multiplication table for n
'''def table_mul(n,i=1):
    if i==10:
        return f"{n} X = {n*i}"
    print(f"{n} X = {n*i}")
    return table_mul(n,i=i+1)
print(table_mul(5))'''
    
# wap to factorial number
'''def fact(n,i=1):
    if i == n:
        return n
    
    return i*fact(n,i=i+1)
print(fact(5))'''

#wap to print all the characters of the string
#while
'''s='hello'
i=0
while i<=len(s)-1:
    print(s[i],end=' ')
    i+=1'''

#recursion
'''def prt_char(s,i=0):
    if i>=len(s)-1:
        return s[i]
    print(s[i],end=' ')
    return prt_char(s,i=i+1)
print(prt_char('hello'))'''

#wap to print all the characters present at even index of the string
#while
'''s='raju'
i=0
while i<=len(s)-1:
    if i%2==0:
        print(s[i],end=' ')
    i+=1'''
#recursion
'''def even_char(s,i=0):
    if i>=len(s)-1:
             return 
    if i%2==0:
       print(s[i],end=' ')
    return even_char(s,i=i+1)
even_char('raju')'''

#wap to extract all the lowercase character present in the string
#while
'''s='GooDMorn'
i=0
while i<=len(s)-1:
    if (97<=ord(s[i])<=122):
        print(s[i])
    i+=1'''
#recursion
'''def lowercase_prt(s,i=0):
    if i>len(s)-1:
        return 
    if(97<=ord(s[i])<=122):
        print(s[i],end=' ')
    return lowercase_prt(s,i=i+1)
lowercase_prt('GooDMorn')'''


#wap to extract  all the vowels present in the string
#while
'''s='junnu'
i=0
while i<=len(s)-1:
    if s[i] in 'aeiou':
        print(s[i],end=' ')
    i+=1

#recursion
def vowel_prt('''


    
        
    

    


