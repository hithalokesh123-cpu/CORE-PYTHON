'''class-->blueprint of an object properties/attributes and functionalities/behaviour
object-->instance/copy of class or real time entity'''
'''class Cname:
    func/pro
obj=Cname(pro1,pro2)'''

'''class School:
    sname='Nazereth'
    loc='bangalore'
    princi='Helda lobo'
    def __init__(self,name,std,phno,addr):
        self.name=name
        self.std=std
        self.phno=phno
        self.addr=addr
    def display(self):
        print('the name is:',self.name)
        print('the std is:',self.std)
        print('the phno is:',self.phno)
        print('the addr is:',self.addr)
    @classmethod
    def show(cls):
        print(cls.sname,cls.loc,cls.princi)
    def ch_phno(self,new):
        self.phno=new
    @staticmethod
    def static():
        print('im a helping method')
    def __call__(self):
        print('object is being called')

s1=School('Nesara',5,9876543212,'CKM')
s2=School('Jitu',6,9988776655,'Guntur')
s3=School('Jyoti',7,6677889955,'Gulbarga')

s1.display()
'''

#inheritance-->single level,multi level,multiple,heirarchical,hybrid
#polymorphism
#encapsulation
#abstraction
#parent/super/base
#child/sub/derived


class Bank:
    bname='ICICI'
    branch='Vijayanagar'
    def __init__(self,name,addr,bal):
        self.name=name         '''initialize the properties'''
        self.addr=addr
        self.bal=bal
class InsufficientBalance(Exception):
    pass

'''single level --one child one parent accessing its properties'''
class NewBank(Bank):
    def __init__(self,name,addr,bal,phno,aadhar):
        self.name=name         '''initialize the properties'''
        self.addr=addr
        self.bal=bal
        self.phno=phno
        self.aadhar=aadhar
    def withdraw(self):
        amount=int(input("enter:"))
        if amount<=self.bal:
            self.bal=self.bal-amount
            print('withdraw successfull')
        else:
            #print('insufficient bal')
            raise InsufficientBalance ('enter lesser amount')



c1=NewBank('Hita','Banalore',10000)

class 







