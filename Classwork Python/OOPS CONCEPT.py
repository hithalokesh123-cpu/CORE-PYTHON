'''class Human:
    eye=2
    ear=2
    nose=1
    brain=1

#obj
Hita=Human()
shreya=Human()'''

#class name access
'''print('class name:',Human.eye,Human.ear,Human.nose,Human.brain)'''

# object name access
'''print('object name:',Hita.eye,Hita.ear,Hita.nose,Hita.brain)'''

#modify the class  new property means adding
'''Human.hands=2
print('human hands:',Human.hands)'''

#modify the object new property means adding particualar property
'''Hita.nose=0
print('obj hitha nose:',Hita.nose)'''

# for all obj create properties for each 
'''Hita.age=21
Hita.contact=5678905678
Hita.addr='bangalore'
Hita.qauli='BCA'
Hita.sweet='Gulab jammu'

shreya.age=22
shreya.contact=12345671234
shreya.addr='Mysuru'
shreya.qauli='BE'
shreya.sweet='Chandrahara'
shreya.color='Blue'
shreya.food='masala dosa'
shreya.dress='modern dress'
shreya.season='summer'''


'''print('obj properties :',Hita.age,Hita.contact,Hita.addr,Hita.qauli)'''

#not defined but still  calling its property
'''thanu.age'''
#error (not defined)


#------------------------CONSTRUCTOR----------------------------------
'''class School:
    school_name='Pentagon space'
    Location=' Vijaynagar Bangalore'
    school_principal='Pradeep Mysuru'

    def __init__(self,age,contact,addr,quali,course):
        self.age=age
        self.contact=contact
        self.addr=addr
        self.quali=quali
        self.course=course
        
hita=School(21,45678956789,'bangalore','BCA','Php')
shreya=School(20,4567890456,'mysuru','BBA','javascript')'''
#hita.addr

#access dict of cname and objname
'''School.__dict__
Hita.__dict__'''

###########################################################################
#TYPES OF METHOD
#OBJECT / INSTANCE
#class method
#static method
#to reduce the repeatedly printing the obj property
'''class School:
    school_name='Pentagon space'
    Location=' Vijaynagar Bangalore'
    school_principal='Pradeep Mysuru'

    def __init__(self,age,contact,addr,quali,course):
        self.age=age
        self.contact=contact
        self.addr=addr
        self.quali=quali
        self.course=course
    # obj method access
    def obj_display(self):
        self.static()
        print(self.age,self.contact,self.addr,self.quali,self.course)

    # obj method modify
    def update_addr(self,new):
        self.addr=new

    #class method
    #class method access
    @classmethod
    def cls_display(cls):
        cls.static()
        print(cls.school_name,cls.Location,cls.school_principal)

    #class method modify
    @classmethod
    def update_Location(cls,new):
        cls.Location=new

    #static method
    @staticmethod
    def static():
        print('the details of:')

hita=School(21,45678956789,'bangalore','BCA','Php')
shreya=School(20,4567890456,'mysuru','BBA','javascript')'''

#instead of printing we are creating the function
'''print(hita=School(21,45678956789,'bangalore','BCA','Php'))
print(shreya=School(20,4567890456,'mysuru','BBA','javascript'))'''

#Output -->calling
#hita.__printobj__()
#shreya.__printojb__()

#problem on banks withraw,deposit,check_balance 
'''class Bank:
    Bank_name='Canara'
    location='madavara'
    Bank_manager='Riya'
    def __init__(self,name,accno,contact,addr):
        self.name=name
        self.accno=accno
        self.contact=contact
        self.addr=addr
        self.bal=0

    def display(self):
        print('Name:',self.name)
        print('Accno:',self.accno)
        print('Contact:',self.contact)
        print('Address:',self.addr)
        print('Balance:',self.bal)

    def deposit(self):
        amount=int(input('Enter the amount:'))
        self.bal=self.bal+amount
        print('Deposited successfully Rs=:',amount)

    def withdraw(self):
       withd_amt=int(input('enter the withdraw amt:'))
       if withd_amt<=self.bal:
           self.bal=self.bal-withd_amt
           print('Withdraw sucessfully')
           print('Your amount is deducted from the account Rs.',withd_amt)
       else:
           print('Insufficient balance')
           print('enter the lesser amt')
    def check_balance(self):
        print('Total balance is:',self.bal)
        
cust1=Bank('Hita',123456789677,898765498,'madnayakanahalli')
cust2=Bank('Kavya',65456789098,876543456,'gayathri nagar')
cust3=Bank('Anish',456789098765,987654322,'dollar colny')'''
    

    
    













