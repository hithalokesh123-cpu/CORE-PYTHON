##--------new mock question-------------------
# program to print all the number which are multiple of 5 from 1 to n
'''n=int(input("enter:"))
i=5
while i<=n:
    print(i)
    i+=5'''
    
#program to print number from n to 1
'''n=int(input("enter:"))
i=n
while i>=1:
    print(i)
    i-=1'''

#program to print sum of individual digit
'''n=int(input("enter:"))
sum=0
while n!=0:
    d=n%10
    n=n//10
    sum=sum+d
print(sum)'''

#find the sum of natural number
'''n=int(input("enter:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)'''

#program to print every char from string
'''s=input("enter:")
index=0
while index<=len(s)-1:
    print(s[index], end=' ')
    index+=1'''


############# normal mock test question ##########################
#wap to print the reverse the word in the sentence
s=input('enter the string:')
out=' '
for i in s.split():
    out+=i[::-1]+' '
print(out.strip())
    
