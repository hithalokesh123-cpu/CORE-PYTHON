'''--------while loop-------------------'''
'''print hello 5 times'''
##s='hello'
##i=1
##while i<=5:
##    print(s)
##    i+=1


'''print 1 to 10'''
##i=1
##while i<=10:
##    print(i)
##    i+=1

'''print from 10 to 1'''
##i=10
##while i>=1:
##    print(i)
##    i-=1

'''print even number between 1 to n'''
##n=int(input("enter:"))
##i=1
##while i<=n:
##    if i%2==0:
##        print(i)
##    i+=1

#wap to extract the char present at even index
'''s='festival'
even-index=' '
i=0
while i<len(s):'''





'''---------------------for loop-----------------------'''
##l=[1,2,'hii',4.5,9,11]
##lis=[]
##for i in l:
##    if type(i)==int:
##        lis.append(i)
##print(lis)             

#wap to extract all the int present in a list
'''l=eval(input('enter:'))
out=[]
for i in l:
    if type(i)==int:
        out.append(i)
print(out)  '''

#wap to reverse string without using slicing
'''s=input('enter:')
rev=''
for ch in s:
    rev=ch+rev
print('Reversed string :',rev)  '''

#wap to remove duplicate from a list

'''l=eval(input('enter:'))
out=[]
for n in l:                   
    if n not in out:
        out.append(n)
print(out)  '''     
    
#wap to convert upper to lower and lower to upper
'''s=input('enter:')
out=' '
for ch in s:
    if 'a'<=ch<='z':
        ch=chr(ord(ch)-32)
    else:
        ch=chr(ord(ch)+32)
    out=out+ch
print(out)'''

#wap to extract the even integer present at odd index of a list
'''l=eval(input('enter:'))
out=[]
for i in range(0,len(l),1):
    if i%2==1:
        if type(l[i])==int:
            if l[i]%2==0:
                out.append(l[i])
print(out)'''

#wap to convert string to dictionary of its index:character
'''s=input('enter:')
d={}
for i in range (len(s)):
    d[i]=s[i]
print(d)'''

#wap to get the following output
#l=['hai',34,3.4,'hello',90,'byebye']
#out={'hai':'hi','hello':'ho','byebye':'be'}
'''l=['hai',34,3.4,'hello',90,'byebye']
d={}
for ch in l:
    if type(ch)==str:
        d[ch]=ch[0]+ch[-1]
print(d)'''

#wap to count the no of occurences of a specific character
'''s=input('enter:')
ch=input('find its frequency character:')
count=0
for c in s:
    if c==ch:
        count+=1
print(f'Frequency of {ch} in {s} is {count}')  '''      

#wap to extract the character in different output variable
'''s=input('enter:')
lower=''
upper=''
digit=''
special_char=''
for ch in s:
    if 'a'<=ch<='z':
        lower+=ch
    elif 'A'<=ch<='Z':
        upper+=ch
    elif '0'<=ch<='9':
        digit+=ch
    else:
        special_char+=ch
print('Upper:',upper)
print('Lower:',lower)
print('Digit:',digit)
print('Special:',special_char) '''   
    
#wap to find the length of collection without using len()
'''l=eval(input('enter:'))
length=0
for i in l:
    length+=1
print(length) '''

#wap to extract all the key value pairs from the dictionary
#only if the keys are of string datatype and values are integer
'''d=eval(input('enter:'))
out={}
for i in d:
    if type(i)==str and type(d[i])==int:
        out[i]=d[i]
print(out)'''

#wap to get the following using len function
#s='power star'
#out{'power':5,'star':4}
'''s='power star'
d={}
word=''
l=0
for i in s:
    if i!=' ':
        word+=i
        l+=1
    else:
        d[word]=l
        word=''
        l=0
d[word]=l
print(d)'''
       
#wap to reverse each word in the string using split() and strip() and join()
'''s='always keep smiling'
out=''
for i in s.split():
    out+=i[::-1]+' '
print(out.strip())'''

'''out=[]
for i in s.split():
    out.append(i[::-1])
print(''.join(s))  '''

#wap to get the following output
#s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
#out=['com','py','html','org']
'''s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
out=[]
for i in s:
   c=i.split('.')
   if c[1] not in out:
       out.append(c[1])
print(out)'''
    
#wap to get the following output.
#In='push maadi kushi padi'
#out={'push':'ph','maadi':'a','kushi':'s','padi':'pi'}
'''s='push maadi kushi padi'
out={}
for i in s.split():
   if len(i)%2==0:
      out[i]=i[0]+i[-1]
   else:
      out[i]=i[1]
print(out)'''

#wap to get the following output
#s=['jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
#out={'com':jiocinema','amazon','py':''file','python','web':'html','org':www}
'''s=['jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
out={}
for i in s:
   c=i.split('.')
   if c[-1] not in out:
      out[c[-1]]=[]
   out[c[-1]].append(c[0])
print(out)'''
   
#wap to find the longest word in the string
'''s='longest sentence'
l=s.split()
long=l[0]
for i in l:
   len(i)>len(long)
   long=i
print(long)'''

#wap to get the following output.
#in='10100011231'
#out='010111000'
'''n='10100011231'
out=''
for i in n:
   if i=='0':
      out+='1'
   elif i=='1':
      out+='0'
print(out)'''


#wap to find the greatest integer in a list of integer
'''l=eval(input('enter:'))
greatest=0
for i in l:
       if i > greatest:
          greatest=i
print('Greatest integer:',greatest)'''


#wap to find the second greatest integer in a list of integer
'''l=eval(input('enter:'))
greatest=0
second=0
for i in l:
   if i>greatest:
      second=greatest
      greatest=i
print('second greatest:',second) '''


'''num=eval(input('enter:'))
greatest=0
second=0
if i in num:
   if i>greatest:
      second=greatest
      greatest=i
   elif i>second and i!=greatest:
      second=num'''

#wap to get the following output.
#in='127342'
#out='242173'(extract even and odd digit separately and concatenate both)
'''inp=input('enter:')
even=''
odd=''
for i in inp:
   if int(i)%2==0:
      even+=i
   else:
      odd+=i
print('Result:',even+odd) '''    

#wap to get the following output.
#in='abacbaacc'
#out={'a':4,'b':2,'c':3}
'''s=input('enter:')
out={}
for c in s:
   if c not in out:
      out[c]=1
   else:
      out[c]+=1
print(out)'''

'''OR'''
#using count and full iteration
'''s=input('enter:')
out={}
for c in s:       #repeats len(s) no. of times
   out[c]=s.count(c)
print(out)'''
   
#OR-more efficient
'''s=input('enter:')
out={}
for c in set(s):       
   out[c]=s.count(c)
print(out)'''
