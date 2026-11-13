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


######################### DAY3 ################################################
#################### MULTI LEVEL INHERITANCE ##################################
#person->employee->manager
'''class person:
    name='janu'
    age =25
class employee(person):
    empid='E312'
    sal=45000
class manager(employee):
    department='hr'
    team_size=10
m1=manager()
print(m1.name)
print(m1.age)
print(m1.empid)
print(m1.sal)
print(m1.department)
print(m1.team_size)'''


#college->department->student
'''class college:
    cname='OPS'
    location='bangalore'
class department(college):
    dname='BCA'
    hod_name='shambbavi'
class student(department):
    std_name='raju'
    roll_no=21
    marks=89
    def grade(self):
        if self.marks>90:
            print("Grade 'A'")
        elif self.marks>80:
            print("Grade 'B'")
        elif self.marks>60:
            print("Grade 'C'")
        else :
            print("Fail")

s1=student()
print(s1.cname)
print(s1.location)
print(s1.dname)
print(s1.hod_name)
print(s1.std_name)
print(s1.roll_no)
print(s1.marks)

s1.grade()'''

#product->Electronic->laptop
'''class product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
   

class electronic(product):
    def __init__(self,pname,price,brand,warranty):
        super().__init__(pname,price)
        self.brand=brand
        self.warranty=warranty
        

class laptop(electronic):
    def __init__(self,pname,price,brand,warranty,processor,ram,storage):
        super().__init__(pname,price,brand,warranty)
        self.processor=processor
        self.ram=ram
        self.storage=storage
    def display(self):
        print(self.pname,self.price,self.brand,self.warranty,self.processor,self.ram,self.storage)

    def finalprice(self):
        gst=self.price*18/100
        finalpr=self.price+gst
        print('The final price is :',finalpr)

l=laptop('laptop',75000,'DELL','6 month','Intel','DDR5','250 TB')
l.display()
l.finalprice()'''

#Employee->Developer->seniorDeveloper
'''class employee:
    def __init__(self,bssal):
        self.bssal=bssal
    def cal_sal(self):
        print('The employee salary is:',self.bssal)

class developer(employee):
    def __init__(self,bssal,devbonus):
        super().__init__(bssal)
        self.devbonus=devbonus
    
    def cal_sal(self):
        db=self.bssal+self.devbonus
        print('The developer salary is :',db)

class seniordeveloper(developer):
    def __init__(self,bssal,devbonus,senbonus):
        super().__init__(bssal,devbonus)
        self.senbonus=senbonus
        
    def cal_sal(self):
        sb=self.bssal+self.devbonus+self.senbonus
        print('The Senior Developer Salary is :',sb)
    
s1=employee(30000)
s2=developer(30000,5000)
s3=seniordeveloper(30000,5000,12000)
s1.cal_sal()
s2.cal_sal()
s3.cal_sal()'''

#product->order->payment
'''
class product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
   

class order(product):
    def __init__(self,pname,price,quantity):
        super().__init__(pname,price)
        self.quantity=quantity
    def cal_tot_price(self):
        tp=self.price*self.quantity
        print('The total price:',tp)

class payment(order):
    def __init__(self,pname,price,quantity,discount,delivery_charge):
        super().__init__(pname,price,quantity)
        self.discount=discount
        self.delivery_charge=delivery_charge
    def display(self):
        print('Product:',self.pname)
        print('Price:',self.price)
        print('Quantity:',self.quantity)
        print('Discount:',self.discount)
        print('Delivery Charge:',self.delivery_charge)

p=payment('Homethether',55000,3,5000,250)
p.display()
p.cal_tot_price()'''
        
############################## DAY 5 ############################################
###################### MULTIPLE INHERITANCE   ##################################
#student result management 
'''class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
    def displayS(self):
        print('Student name:',self.name)
        print('Rollno:',self.roll_no)
        return self 

class Academic:
    def __init__(self,marks):
        self.marks=marks
        
    def displayA(self):
        print('Academic marks:',self.marks)
        return self

class Sports:
    def __init__(self,sports_marks):
        self.sports_marks=sports_marks
        
    def displaySP(self):
        print('Sports marks:',self.sports_marks)
        return self

class Result(Student,Academic,Sports):
    def __init__(self,name,roll_no,marks,sports_marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.sports_marks=sports_marks

    def totalmar(self):
        tm=self.marks+self.sports_marks
        print('Total Marks:',tm)
        return self

stud1=Result('Mohan',31,420,45)
stud1.displayS() .displayA() .displaySP() .totalmar()'''

#Banking System
'''class Account:
    def __init__(self,accno):
        self.accno=accno
    def display_acc(self):
        print('Account number:',self.accno)
        return self

class Customer:
    def __init__(self,cust_name):
        self.cust_name=cust_name
    def display_cust(self):
        print('Customer name:',self.cust_name)
        return self
        
class Transaction:
    def __init__(self,bal):
        self.bal=bal
    def display_Bal(self):
        print('Balance:',self.bal)
        return self

class BankDetails(Account,Customer,Transaction):
    def __init__(self,accno,cust_name,bal):
        Account.__init__(self,accno)
        Customer.__init__(self,cust_name)
        Transaction.__init__(self,bal)

cust1=BankDetails(1234567890987654,'Muniraju',525000)
cust1.display_acc() .display_cust() .display_Bal()'''

################# Day 6 ###########################
################# DECORATOR  ######################
#Write a decorator to print message befor and after exceution the function
'''def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('Before exceuting the function')
        func(*args,**kwargs)
        print('After executing the function')
    return wrapper
    
@my_decorator
def greet():
    print('Hello.Welcome to python')

greet()'''

#Write a decorator to calculate the exceution time or simply count
# how many times a function is called
'''def count_calls(func):
    count=0
    def wrapper(*args,**kwargs):
       nonlocal count
       func(*args,**kwargs)
       count+=1
       print(f'Function called {count} times')
    return wrapper

@count_calls
def greet():
    print('hello!')

greet()
greet()
greet()
greet()'''

#write a decorator named check_age that checks whether a person is eligible to vote
'''def check_age(func):
    def wrapper(*args,**kwargs):
        if args[0]>=18:
           func(*args,**kwargs)
        else:
            print('You are not eligible to vote')
    return wrapper

@check_age
def vote(age):
    print('You are eligible to vote')

vote(25)
vote(16)'''

#create function dashboard()that displays
#output
#Welcome to your dashboard!
#please login first!

'''def dashboard(func):
    def wrapper(*args,**kwargs):
        if args[0] == True:
            func(*args,**kwargs)
        else:
            print('Please Login first!')
    return wrapper

@dashboard
def login(is_logged_in):
    print('Welcome to your dashboard')

login(False)
login(True)'''

#DECORATOR to validate the function arguments
'''def positive_number(func):
    def wrapper(*args,**kwargs):
        for i in args:
          if i <= 0:
              print("Negative number are not allowed!")
              return
          
        func(*args,**kwargs)
    return wrapper

@positive_number
def multiply(a,b):
    result=a*b
    print('Result:',result)
    
multiply(5,2)
multiply(10,-2)
multiply(4,6)
multiply(-4,6)'''

#Create a decorator named retry that allows a function to exceute a maximum of 3 times if it fails
'''def retry(func):
    def wrapper(*args,**kwargs):
        for i in range(1,5):
            print('Attempt:',i)
            try:
                coonection=func(*args,**kwargs)
                if connection ==  True:
                    print('Server connected successfully')
                    return
                else :
                    print("Connection failed! Retrying...")
            except:
                print('Connection failed! Retrying...')
        print('Unable to connect to server')
    return wrapper

@retry
def connect_server():
    return True

connect_server()'''


############################# DAY 7 #########################################
############################## oops method ##################################
# Employee to manage employee details
class Employee:
    company_name='Infosys'
    total_employees=0

    def __init__(self,empid,ename,sal):
        self.empid=empid
        self.ename=ename
        self.sal=sal

        Employee.total_employees += 1

    def display_details(self):
        print('Employee id:',self.empid)
        print('Employee name:',self.ename)
        print('Salary:',self.sal)
        print('Company name:',Employee.company_name)

    @classmethod
    def totalemployee(cls):
        print('Total Employees:',Employee.total_employees)

    @classmethod
    def change_company_name(cls,new):
        print('After changing company:')
        cls.company_name=new
        print()
        print('Company:',cls.company_name)

    @staticmethod
    def check_salary(sal):
        if sal>=25000:
            return 'Eligible'
        else:
            return 'Not Eligible'

e1=Employee('101','Raju',25000)
e2=Employee('102','Janvi',45000)
e1.display_details()
print()
e2.display_details()
print()
Employee.totalemployee()
print()
Employee.change_company_name('TCS')
print()
print('Salary Eligibility:')
print('Raju:',Employee.check_salary(e1.sal))
print('Janvi:',Employee.check_salary(e2.sal))        

