'''---write program on area of rectangle------ '''
##a=eval(input("enter length:"))
##b=eval(input("enter breadth:"))
##print("The area of rectangle: ",a*b)

'''----write program on reverse string-----'''
##s=input("enter string: ")
##print (" the  reversed string is : " ,s[::-1])
   
'''----WRITE PROGRAM ON PERIMETER OF SQUARE-----'''
##side=eval(input("enter the side value:"))
##print ("The perimeter of square: ",4*side)

      
'''------------if condition-------------------'''
##age=int(input("enter your age:"))
##if age>=18:
##    print("your are eligible")

##num=eval(input("enter the number:"))
##if num>=0:
##    print ("The given numer is positive")

##num=int(input("enter the number:"))
##if(num%2==0):
##    print("Square is",num**2,"it is even")

##ch=str(input("enter the single character:"))
##if ch in 'aeiouAEIOU':
##    print(ch,'is vowel')

'''----------------if else condition-----------------'''
##num=eval(input("enter the number:"))
##if num%2==0:
##    print("Square is",num**2,"it is even")
##else:
##    print("Cube is",num**3,"it is even")


##ch=input("enter:")
##if ch>='A' and ch<='Z':
##    print(ch,"is uppercase")
##else:
##    print(ch,"is lowercase")

##ch=input("enter:")
##c=ord(ch)
##if c>=97:
##    print(ch,"is lowercase")
##else:
##    print(ch,"is uppercase")


##ch=input("enter:")
##if ch>='0' and ch<='9':
##    print(ch,"it is digit")
##else:
##    print(ch,"it is not digit")

##n=int(input("enter:"))
##if n%3==0 and n%5==0:
##    print(n,"it is divisible by both 3 and 5")
##else:
##    print(n,"it is not divisible by both 3 and 5")


##s=input("enter a string:")
##import keyword
##if s in keyword.kwlist:
##    print(f"{s} is a keyword")
##else:
##    print(f"{s} is not keyword")

   
##ch=input("enter a character:")
##if not('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9':
##       print(f"{ch} it is a special character")
##else:
##    print(f"{ch} it is not special character")

##s=input("enter a string")
##if s == s[::-1]:
##    print(s,"is pallindrome",s[::-1])
##else:
##    print(s,"is not pallindrome",s[::-1])
##       


##a=eval(input("enter:"))
##if  (type(a)==list or type(a)==dict or type(a)==set):
##    print(a ,"is a mutable data type")
##else:
##    print(a,"is not mutable data type")



##if (1,2,3)is (1,2,3) :
##    print("pointing to the same memory")
##else:
##    print("not pointing to the same memory")
    
##l=eval(input("enter:"))
##lis=len(l)
##if (lis%2==0):                  
##    print("no middle value",l[len(l)//2])
##else:
##    print("middle value")
##



##'''--------------------------elif cond--------------------------'''
##
##ch=input("enter charater:")
##if 'A'<=ch<='Z':
##         print("uppercase:",ch)
##elif 'a'<=ch<='z':
##         print("lowercase:",ch)
##elif '0'<=ch<='9':
##         print("digit:",ch)
##else:
##    print("special character:",ch)



##n=int(input("enter any digit:"))
##if 0<=n<=9:
##    print("single digit:",n)
##elif 10<=n<=99:
##    print("double digit:",n)
##elif 100<=n<=999:
##    print("triple digit:",n)
##else:
##    print(" more than 3 digit:",n)
    
         
##n=abs(int(input("enter any digit:")))
##if 0<=n<=9:
##    print("single digit:",n)
##elif 10<=n<=99:
##    print("double digit:",n)
##elif 100<=n<=999:
##    print("triple digit:",n)
##else:
##    print(" more than 3 digit:",n)


##string approach
##s=str(n)
##if len(s)==1:
##    print('single')
##elif len(s)==2:
##    print("double")
##elif len(s)==3:
##    print("triple")
##else:
##    print(" more than 3 digit")


##x=int(input("enter:"))
##y=int(input("enter:"))
##if  x==0 and y==0:
##    print("origin",x,y)
##elif  x>0 and y>0:
##    print("Quadrant-1:",x,y)
##elif  x<0 and y>0:
##    print("Quadrant-2:",x,y)
##elif  x<0 and y<0:
##    print("Quadrant-3:",x,y)
##elif  x>0 and y<0:
##    print("Quadrant-4:",x,y)
##elif  x==0 and y>0:
##    print("lie on y-axis:",x,y)
##elif  x>0 and y==0:
##    print("lie on x-axis:",x,y)    

    
'''wap to print fizz if the number multiple of 3,print buzz if number is multiple of 5 and print fizzbuzz if it is multiple of 3 and 5'''
##num=int(input("enter:"))
##if num%3==0 and num%5==0:
##    print("Fizzbuzz")
##elif num%3==0:
##    print("Fizz")
##elif num%5==0:
##    print("Buzz")
##else:
##    print ("not multiple by both 3 and 5")


'''wap to find greatest of 3 number'''
##n1=int(input("enter 1st number:"))
##n2=int(input("enter 2st number:"))
##n3=int(input("enter 3st number:"))
##if n1==n2==n3:
##      print("all are equal")
##elif n2<n1>n3:
##    print(n1,"is greater")
##elif n2>n3:
##    print(n2,"is greater")
##else:
##    print(n3,"is greater")


'''wap to check whether to convert uppercase---lowercase,lowercase--uppercase,digit---square of it,special character----print for 5 times '''
##ch=input("enter charater:")
##if 'A'<=ch<='Z':
##         print("uppercase to lowercase:",chr(ord(ch)+32))
##elif 'a'<=ch<='z':
##         print("lowercase to uppercase:",chr(ord(ch)-32))
##elif '0'<=ch<='9':
##         print("digit",int(ch)**2)
##else:
##    print("special character:",ch*5)


'''wap to check whether the character is vowel or consonant'''
##ch=input("enter:")
##if 'a'<=ch<='z'or'A'<=ch<='Z':
##    if ch in 'aeiouAEIOU':
##        print(ch,'is vowel')
##    else:
##        print(ch,'is consonent')
##else:
##    print(ch,'not an alphabet')

'''wap to print middle value of a list if it is string and check palindrome or not '''
##lis=eval(input("enter:"))
##if len(lis)%2==1:
##    print("it is middle value")
##    mid_val=lis[len(lis)//2]
##    if type(mid_val)==str:
##        print('it is string')
##        if mid_val==mid_val[::-1]:
##            print("it is palindrome",mid_val[::-1])
##        else:
##            print("it is not palindrome")
##    else:
##        print("it is not string")
##else:
##    print("it is not middle value")

'''wap to print the reversed string if it is starting with vowel and ending with
special character.'''
s=input("enter:")
if s[0] in 'aeiouAEIOU':
    print("it is start with vowel")
    ch=s[len(s)-1]
    if  not ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
        print("it is end with special character")
        print("the reversed string is ",s[::-1])
    else:
        print("it is  not end with special character")
else:
     print("it is not start with vowel")

