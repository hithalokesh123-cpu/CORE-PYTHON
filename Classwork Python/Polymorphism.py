#---------------------- POLYMORPHISM------------------------------------
##################### COMPLIE-TIME/METHOD OVERLOADING ######################
'''def sam(a,b):
    print(a+b)
def sam(a,b,c):
    print(a+b-c)
def sam(a,b,c,d):
    print(a+b,c+d)
sam(10,20)'''
#TypeError: sam() missing 2 required positional arguments: 'c' and 'd'
#method overloading is not support in python ,but it act as run-time polymorphism

#it can be achieved by copy operation()
'''def sam(a,b):
    print(a+b)
temp1=sam
def sam(a,b,c):
    print(a+b-c)
temp2=sam
def sam(a,b,c,d):
    print(a+b,c+d)
temp1(10,20)
temp2(10,20,40)
sam(20,40,20,40)'''

##################  METHOD OVERRIDING ######################################
'''class Parent:
    def sam(self):
        print('im from parent class')
ob1=Parent()
class Child(Parent):
    def sam(self):
        print('im from parent class')
    def child(self):
        print('hello everyone')
ob=Child()
ob.sam()
ob.child()'''


########################## ducktyping  ###########################
'''class Dog:
    def sound(self):
        print('bow bow')
class Cat:
    def sound(self):
        print('meow meow')
c=Cat()
d=Dog()

def make_sound(obj):
    obj.sound()

c.sound()
d.sound()'''

#################### OPERATOR LOADING #################################
# dir(int)
'''class Sam:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    def __mod__(self,other):
        return self.a%other.a
    
    def __eq__(self,value):
        return self.a==value
    def __ge__(self,value):
        return self.a >= value
    

    

x=Sam(10)
y=Sam(20)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)

print(x==y)
print(x >= y)'''






#dir(list)
'''class sam:
    def __init__(self,x):
        self.x=x
    def __len__(self):
        return len(self.x)
    def __getitem__(self,index):
        return self.x[index]
    def __setitem__(self,index,new):
        self.x[index]=new
    def __contains__(self,val):
        return val in self.x
    def __str__(self):
        return 'Object is belongs to sam class'
    def __call__(self):
        return 'Oject is being callable'
ob=sam([1,2,3,4])
print(len(ob))
print(ob[1])
ob[2]=200
print(ob.x)
print(2 in ob)
print(10 in ob)
print(ob)
print(ob())'''


############################## ENCAPSULATION #############################
######## PUBLIC ACCESS SPECIFIER #########
'''class Bank:
    bname='SBI'
    branch="vijaynagar"
    manager='Sanju'
    ifsc="sbi110031"
    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.phno=phno
        self.accno=accno
        self.bal=bal
    @classmethod
    def display(cls):
        print(cls.bname,cls.branch,cls.manager,cls.ifsc)

c1=Bank('hita',45676567890,998765432345678,6500000)

Bank.display()
print(c1.name)
print(c1.bal)
print(c1.accno)
print(c1.phno)'''
    

######## PROTECTED ACCESS SPECIFIER #########
'''class Bank:
    bname='SBI'
    branch="vijaynagar"
    _manager='Sanju'
    ifsc="sbi110031"
    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.phno=phno
        self.accno=accno
        self._bal=bal
    @classmethod
    def display(cls):
        print(cls.bname,cls.branch,cls._manager,cls.ifsc)

c1=Bank('hita',45676567890,998765432345678,6500000)

Bank.display()
#print(c1.bal)         --------> error in display() _manager
#print(Bank.manager)  ----------> error  print
print(c1._bal)
print(Bank._manager)'''

######## PRivate ACCESS SPECIFIER  1 way to name mangling #########
'''class Bank:
    bname='SBI'
    __branch="vijaynagar"
    _manager='Sanju'
    ifsc="sbi110031"
    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.__phno=phno
        self.__accno=accno
        self._bal=bal
    @classmethod
    def display(cls):
        print(cls.bname,cls.__branch,cls._manager,cls.ifsc)

c1=Bank('hita',45676567890,998765432345678,6500000)

Bank.display()
print(Bank._Bank__branch)
print(c1._Bank__accno)
print(c1._Bank__phno)'''

########### 2 way to access private access modifier ---> public method/functon ##################
'''class Bank:
    bname='SBI'
    __branch="vijaynagar"
    _manager='Sanju'
    ifsc="sbi110031"
    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.__phno=phno
        self.__accno=accno
        self._bal=bal
    @classmethod
    def display(cls):
        print(cls.bname,cls.__branch,cls._manager,cls.ifsc)
    def get_accno(self):
        print(self.__accno)
    def set_phno(self,new):
        self.__phno=new
    def get_phno(self):
        print(self.__phno)

c1=Bank('hita',45676567890,998765432345678,6500000)
Bank.display()
c1.get_accno()
c1.set_phno(87654326788)
c1.get_phno()'''


################## 3 way using access-->@ property and modify--->@attr.setter ###################################
'''class Bank:
    bname='SBI'
    __branch="vijaynagar"
    _manager='Sanju'
    ifsc="sbi110031"
    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.__phno=phno
        self.__accno=accno
        self._bal=bal
    @classmethod
    def display(cls):
        print(cls.bname,cls.__branch,cls._manager,cls.ifsc)

    @property
    def phno(self):
        print(self.__phno)
    @phno.setter
    def phno(self,new):
        self.__phno=new
        
c1=Bank('hita',45676567890,998765432345678,6500000)
Bank.display()
c1.phno=75345678995
c1.phno'''

########################### ABSTRACTION ###############################
'''from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def check_bal():
        pass
    @abstractmethod
    def withdraw():
        pass
    @abstractmethod
    def deposit():
        pass
    @abstractmethod
    def update_pin():
        pass

class NewAtm(ATM):
    name='ICICI'
    loc='bangalore'
    def __init__(self,name,accno,pin,bal):
        self.name=name
        self.accno=accno
        self.pin=pin
        self.bal=bal
    def check_bal(self):
        p=int(input('enter your atm pin:'))
        if p==self.pin:
            print('the available balance is :',self.bal)
        else:
            print('invalid pin')
            
    def update_pin(self):
        p=int(input('enter your existing atm pin:'))
        if p==self.pin:
            new=int(input('enter your new pin:'))
            self.pin=new
            print('pin updated successfully')
        else:
            print('invalid pin')

    def deposit(self):
        p=int(input('enter your existing atm pin:'))
        if p==self.pin:
            amount=int(input('enter the amount to deposit:'))
            self.bal+=amount
            print("deposited successfully")
        else:
            print('invalid pin')

    def withdraw(self):
        p=int(input('enter your existing atm pin:'))
        if p==self.pin:
            amount=int(input('enter the amount to deposit:'))
            if self.bal>=amount:
                self.bal-+amount
                print('withdraw successfully')
            else:
                print('insufficient balance')
        else:
            print('invalid pin')


c1=NewAtm('harshu',345678909876543,1234,25000)

def operations(obj):
         print('enter 1 to check_bal')
         print('enter 2 to update_pin')
         print('enter 3 to withdraw' )
         print('enter 4 to deposit')
         print('enter 5 to stop')
         while True:
                   choice=int(input("enter you choice:"))
                   if choice==1:
                       obj.check_bal()
                   elif choice==2:
                       obj.update_pin()
                   elif choice==3:
                       obj.withdraw()
                   elif choice==4:
                       obj.deposit()
                   elif choice==5:
                       return 'thank you for using'
                   else:
                       print('invalid choice')'''
    
          

            
            
        
       

    
    
        


