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

#################### DAY 2 ########################
#Count the number of digits in a given number
'''n=45678
count=0
while n>0:
    d=n%10
    count+=1
    n//=10
print(count)'''

#print the multiplication table of a given number using a while loop
'''i=1
while i<=10:
    print(f'{5} X {i} ={5*i}')
    i+=1'''
    
#Find the sum of all even digits in a given number using a while loop
'''n=123456
sum=0
while n>0:
    d=n%10
    if d%2==0:
        sum+=d
    n//=10
print(sum) '''       

#count how many even digit and odd digit are present in a given number
'''n=123456
even_no=0
odd_no=0
while n>0:
    d=n%10
    if d%2==0:
        even_no+=1
    else:
        odd_no+=1
    n//=10
print('Even digits:',even_no)
print('Odd digits:',odd_no) '''

#reverse the string using while loop
'''s='python'
rev=" "
i=0
while i<len(s):
    rev=s[i]+rev
    i+=1
print(rev)'''

#check whether the number is a perfect number using while loop
'''n=6
temp=n
sum=0
i=1
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum == temp:
    print('it is perfect number',temp)
else:
    print('it is not perfect number',temp)'''

#check whether the number is a strong number using while loop
'''n=145
temp=n
sum=0
while n>0:
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact
    n//=10
if sum == temp:
    print('it is strong number',temp)
else:
    print('it is not strong number',temp)'''

#check whether the number is a armstrong number using while loop
'''n=153
temp=n
sum=0
length=len(str(n))
while n>0:
    d=n%10
    a=d**length
    sum+=a
    n//=10
if sum == temp:
    print('it is armstrong number',temp)
else:
    print('it is not armstrong number',temp)'''


#find the largest digit in the given number using a while loop
'''n=58329
largest=0
while n>0:
    d=n%10
    if d >largest:
         largest = d
    n//=10
print('Largest digit:',largest)'''    

#find the smallest digit in the given number using a while loop
'''n=58329
small=9
while n>0:
    d=n%10
    if d < small:
        small=d
    n//=10
print('Smallest digit:',small)'''


########################### DAY 3 ############################################
########################## SINGLE LEVEL INHERITANCE ##########################
#PERSON AND STUDENT
'''class Person:
    name='mala'
    age=40
    
class child(Person):
    rollno=121
    
student=child()
print(student.name)
print(student.age)
print(student.rollno)'''

#employee and manager
'''class Employee:
    empid='E101'
    ename='Rahul'
    salary=30000

class Manager(Employee):
    department='Marketing'
    Team_size=10

per=Manager()
print('Employee ID:',per.empid)
print('Employee Name:',per.ename)
print('Salary:',per.salary)
print('Department:',per.department)
print('Team Size:',per.Team_size)'''

#bank acc and saving acc
'''class BankAcc:
    accno=2345678987654322
    holder_name='Ramya'
    balance=50000
    def display(self):
        print(self.accno,self.holder_name,self.balance,end='\n')

class SavingAcc(BankAcc):
    interest_rate=5
    account_type='saving'

cust=SavingAcc()
cust.display()
print(cust.interest_rate)
print(cust.account_type)'''


#Company and developers
'''class Company:
    cname='RADO'
    location='Bangalore'
    CEO='Mallesh'
    def display(self):
        print('Company name :',self.cname)
        print('Location:',self.location)
        print('CEO:',self.CEO)

class Developer(Company):
    role='junior developer'
    dname='bablu'

employee=Developer()
employee.display()
print('Employee role:',employee.role)
print('Name:',employee.dname)'''

#employee salary calculation
'''class Employee:
    def __init__(self,empid,ename,basic_salary):
        self.empid=empid
        self.ename=ename
        self.basic_salary=basic_salary
    def display_details(self):
        print(self.empid,self.ename,self.basic_salary)
class Developer(Employee):
   def __init__(self,empid,ename,basic_salary,role,bonus):
       super().__init__(empid,ename,basic_salary)
       self.role=role
       self.bonus=bonus
   def Total_sal(self):
       total_sal=self.basic_salary+self.bonus
       print('the total salary is:',total_sal)

e1=Developer('E121','mohan',25000,'junior developer',10000)
e1.display_details()
print()
e1.Total_sal()'''
