################### EXCEPTION ######################
############# SPECIFIC ERROR #######################
#ValueError
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))

except ValueError as e:
    print(e)

else:
    print(a+b)
    print('no error is found')

finally:
    print('exceution completed')'''

#NameError
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a+c)
    

except ValueError as e:
     print(e)
except NameError as e:
    print(e)

else:
    print('no error is found')

finally:
    print('exceution completed')'''


#ZeroDivisionError
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
    

except ValueError as e:
     print(e)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

else:
    print('no error is found')

finally:
    print('exceution completed')'''


##################### generic except block  ###########################
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    #print(a/b)
    #print(a+c)
    print(a+b)

except Exception as e:
    print(e)

else:
    print('no error is found')

finally:
    print('exceution completed')'''

#not handle the KeyboardInterrupt it can be handle using Specific except block
'''try:
   for i in range(1,1000):
           print(i)
except Exception as e:
    print(e)

else:
    print('no error is found')

finally:
    print('exceution completed')'''

#output-KeyboardInterrupt

#KeyboardInterrupt it can be handle using Specific except block
'''try:
   for i in range(1,1000):
           print(i)
except KeyboardInterrupt:
    print('user should stop')           
except Exception as e:
    print(e)

else:
    print('no error is found')

finally:
    print('exceution completed')'''

##################### bared/default except block #####################
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
    for i in range(1,1000):
            print(i)
         
except:
    print('error handled')

else:
    print('no error is found')

finally:
    print('exceution completed')'''

####### RAISE ERROR ################
#### Custm Error #######
#Create a NotPallindrome error raise it if the str is not pallindrome 
'''class NotPallindrome(Exception):
    pass
s=input("enter a string:")
word=''
for i in s:
    word=i[::-1]+word
if s == word:
    print (word, 'it is  pallindrome')
else:
    raise NotPallindrome('it is not pallindrome')'''

#Create bank class with withdraw method user enter amt to withdraw, if amt> bal raise error
'''class InsuffientBal(Exception):
    pass
class Bank:
    bal=40000
    def withdraw(self):
        amt=int(input('Enter the withdraw amount:'))
        if amt < self.bal :
           self.bal=self.bal-amt
           print('The total balance',self.bal)
        else:
            raise InsuffientBal ('InSufficient Amount')

        
cust1=Bank()
cust1.withdraw()'''

#ASSERTION Error
'''bal=30000
amt=int(input('Enter the withdraw amount:'))
assert amt < bal,'InSufficient Amount'
bal=bal-amt
print('The total balance',self.bal)'''


