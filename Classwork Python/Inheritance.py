#--------INHERITANCE--------
#-------SINGLE LEVEL--------
#program
'''class Vehicle:
    brand='TATA'
    fuel_type='petrol'
    def ride(self):
        print('today Im going to ride')

class scooty(Vehicle):
    color:'red'
    price:150000
    model:2007
    wheel=2
    mode='electric'
    brand='jupiter'
    def start(self):
        print('the vehicle is starting')
u1=scooty()
u1.start()
u1.brand
u1.price'''

# simple program
'''class Human:
    eye=2
    ear=2
    nose=1
    
class girl(Human):
    hair_type='long_hair'
    hair_color='black'
    dress='saree'

riya=girl()'''

############################### MULTI LEVEL ###########################################

# Constructor chaining concept is used instead of again and again initializing the parent property to the current class
#we can use the super().__init__(previous  super_class properties............)
'''class Resume_10:
    def __init__(self,name,contact,email,per_10,year_10,sname,board_10):
        self.name=name
        self.contact=contact
        self.email=email
        self.per_10=per_10
        self.year_10=year_10
        self.sname=sname
        self.board_10=board_10

    def display_10(self):
        print(self.name,self.contact,self.email,self.per_10,self.year_10,self.sname,self.board_10,sep='\n')

    def update_contact(self,new):
        self.contact=new
        

class Resume_12(Resume_10):
    def __init__(self,name,contact,email,per_10,year_10,sname,board_10,per_12,yop_12,cname_12,board_12):
        super().__init__(name,contact,email,per_10,year_10,sname,board_10)
        self.per_12=per_12
        self.yop_12=yop_12
        self.cname_12=cname_12
        self.board_12=board_12

    def display_12(self):
        print(self.per_12,self.yop_12,self.cname_12,self.board_12,sep='\n')
    
class Resume_degree(Resume_12):
    def __init__(self,name,contact,email,per_10,year_10,sname,board_10,per_12,yop_12,cname_12,board_12,cgpa,yop,college,university):
         super().__init__(name,contact,email,per_10,year_10,sname,board_10,per_12,yop_12,cname_12,board_12)
         self.cgpa=cgpa
         self.yop=yop
         self.college=college
         self.university=university

    def display_degree(self):
        print(self.cgpa,self.yop,self.college,self.university,sep='\n')



s1=Resume_degree('hita',34567893456,'hi123@gmaoil.com',81,2020,'Oxford school','ICSE',96.83,2023,'ascent pu college','PUC',9.5,2026,'mlacw','BCU')
s1.display_10()
print("************************")
s1.display_12()
print("************************")
s1.display_degree()'''



#   METHOD CHAINING (INVOKING THE PARENT CLASS METHOD IN CHILD CLASS)
'''class Resume_10:
    def __init__(self,name,contact,email,per_10,year_10,sname,board_10):
        self.name=name
        self.contact=contact
        self.email=email
        self.per_10=per_10
        self.year_10=year_10
        self.sname=sname
        self.board_10=board_10

    def display(self):
        print(self.name,self.contact,self.email,self.per_10,self.year_10,self.sname,self.board_10,sep='\n')

    def update_contact(self,new):
        self.contact=new
        

class Resume_12(Resume_10):
    def __init__(self,name,contact,email,per_10,year_10,sname,board_10,per_12,yop_12,cname_12,board_12):
        super().__init__(name,contact,email,per_10,year_10,sname,board_10)
        self.per_12=per_12
        self.yop_12=yop_12
        self.cname_12=cname_12
        self.board_12=board_12

    def display(self):
        super().display()
        print(self.per_12,self.yop_12,self.cname_12,self.board_12,sep='\n')
    
class Resume_degree(Resume_12):
    def __init__(self,name,contact,email,per_10,year_10,sname,board_10,per_12,yop_12,cname_12,board_12,cgpa,yop,college,university):
         super().__init__(name,contact,email,per_10,year_10,sname,board_10,per_12,yop_12,cname_12,board_12)
         self.cgpa=cgpa
         self.yop=yop
         self.college=college
         self.university=universit

    def display(self):
        super().display()
        print(self.cgpa,self.yop,self.college,self.university,sep='\n')



s1=Resume_degree('hita',34567893456,'hi123@gmaoil.com',81,2020,'Oxford school','ICSE',96.83,2023,'ascent pu college','PUC',9.5,2026,'mlacw','BCU')
s1.display()'''

############################################# MULTIPLE INHERITANCE ##############################################
'''class Batsman:
    def __init__(self,name,team,age,runs,century):
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century

    def bat(self):
        print(self.name,'is batting')

class Bowler:
    def __init__(self,name,team,age,wickets,dot_balls):
        self.name=name
        self.team=team
        self.age=age
        self.wickets=wickets
        self.dot_balls=dot_balls

    def bowl(self):
        print(self.name,'is bowling')

class AllRounder(Bowler,Batsman):
    def __init__(self,name,team,age,runs,century,wickets,dot_balls):
        #super().__init__(wickets,dot_balls)
        
        #this will give error due  to as we  have mention in the child class(batsman,bowler)
        #in the batsman class it will check for  wickets and dot balls , so it gives the error)
        #instead we will again initialize that attribute in the child class
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century
        self.wickets=wickets
        self.dot_balls=dot_balls
        
    def field(self):
        print(self.name,'is fielding')


person=AllRounder('KL Rahul','Delhi',32,5000,16,550,350)

person.bat()
print()
person.bowl()
print()
person.field()'''

#---------****************  METHOD CHAINING  *******************--------------
'''class Batsman:
    def __init__(self,name,team,age,runs,century):
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century

    def bat(self):
        print(self.name,'is batting')
        return self

class Bowler:
    def __init__(self,name,team,age,wickets,dot_balls):
        self.name=name
        self.team=team
        self.age=age
        self.wickets=wickets
        self.dot_balls=dot_balls

    def bowl(self):
        print(self.name,'is bowling')
        return self

class AllRounder(Bowler,Batsman):
    def __init__(self,name,team,age,runs,century,wickets,dot_balls):
        
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century
        self.wickets=wickets
        self.dot_balls=dot_balls
        
    def field(self):
        print(self.name,'is fielding')
        return self


person=AllRounder('KL Rahul','Delhi',32,5000,16,550,350)
person.bat() .bowl() .field()'''

#access mro
##print(AllRounder.mro())
##print(AllRounder.__mro__)

####################### HIERARCHICAL INHERITANCE #####################################
'''class Company:
    def __init__(self,com_name,location,ceo,type_company):
        self.com_name=com_name
        self.location=location
        self.ceo=ceo
        self.type_company=type_company

    def display(self):
        print('Company Name:',self.com_name)
        print('Location:',self.location)
        print('CEO of Company:',self.ceo)
        print('Company Type:',self.type_company)

class SalesDept(Company):
    def __init__(self,com_name,location,ceo,type_company,staff_count,product_name,sale_mgr_name):
        super().__init__(com_name,location,ceo,type_company)
        self.staff_count=staff_count
        self.product_name=product_name
        self.sale_mgr_name=sale_mgr_name

    def display_s(self):
        super().display()
        print('Sales staff count:',self.staff_count)
        print('Product Name:',self.product_name)
        print('Sales Manager name:',self.sale_mgr_name)

class DigitalMarketing(Company):
    def __init__(self,com_name,location,ceo,type_company,D_team_member_count,digital_mgr_name):
        super().__init__(com_name,location,ceo,type_company)
        self.D_team_member_count=D_team_member_count
        self.digital_mgr_name=digital_mgr_name

    def display_d(self):
        super().display()
        print('Digital team member count:',self.D_team_member_count)
        print('Digital Manager Name:',self.digital_mgr_name)


class Finance(Company):
    def __init__(self,com_name,location,ceo,type_company,F_team_count,Finance_mgr_name):
        super().__init__(com_name,location,ceo,type_company)
        self.F_team_count=F_team_count
        self.Finance_mgr_name=Finance_mgr_name

    def display_f(self):
        super().display()
        print('Finance team member count:',self.F_team_count)
        print('Digital Manager Name:',self.Finance_mgr_name)
        
        

user1=SalesDept('ABC Company','JP Nagar','Hita Achar','Service based Company',25,'perfume','Rishi')
user2=DigitalMarketing('ABC Company','JP Nagar','Hita','Service based Company',15,'Ridhi Mallesh')
user3=Finance('ABC Company','JP Nagar','Hita','Service based Company',2,'Rahul Bharathwaj')
user1.display_s()
print()
user2.display_d()
print()
user3.display_f()'''


###########################  HYBRID INHERITANCE  #####################################################
'''class College:
    def College_name(self):
        print('Mlacw College')
        return self

class BCA(College):
    def BCA_dept(self):
        print('BCA department')
        return self

class BSC(College):
    def BSC_dept(self):
        print('BSC Department')
        return self

class HOD(BCA,BSC):
    def HOD_dept(self):
        print('Head of Department')
        return self

stud=HOD()
stud.College_name() .BCA_dept() .BSC_dept() .HOD_dept()'''











        

    


