##-------------NESTED  LOOP--------------------

'''for i in range (1,10,2):
    for j in range (1,10,3):
        print(i,j)'''

#1,3,5,7,9=i
#1,4,7=j
#no of iteration 5*3=15

'''s='hello'
for i in s:
    for j in s:
        print(i+j)

c=0
for i in range(1,15,3):
    for j in range(2,20,4):
        for k in range(5,50,10):
            print(i+j+k)
            c+=1'''
        
    
#interview
#wap to flatten a nested list
'''l=[[1,2,3],[4,5,6],[7,8,9]]
out=[1,2,3,4,5,6,7,8,9]
flatten_list=[]
for i in l:
    for j in i:
        flatten_list.append(j)
print(flatten_list) '''      


#wap to get the following output.without length function
#s='power star'
#out={'power':5,'star':4}
'''s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        count+=1
    out[i]=count
print(out)'''

#wap to get the following output.
#s='power star'
#out={'power':2,'star':1}
'''s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        if j  in 'AEIOUaeiou':
            count+=1
            out[i]=count
print(out) '''

#'power':['rewop',2,'pwr']
#'star': ['rats', 1, 'sa']
'''s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        if j  in 'AEIOUaeiou':
            count+=1
            out[i]=[i[::-1],count,i[::2]]
print(out)'''

#wap to get the following output.
#in=['hello',227,3.4,'last',189,34]
#out=[722,981,43]
'''l=['hello',227,3.4,'last',189,34]
out=[]
for i in l:
    if type(i)==int:
        rev=0
        while i>0:
            d=i%10
            rev=(rev*10)+d
            i=i//10
        out.append(rev)
print(out)'''


#not efficient way 
'''l=['hello',227,3.4,'last',189,34]
out=[]
for i in l:
    if type(i)==int:
       rev=str(i)[::-1]
       out.append(int(rev))
print(out)'''

##-----------------ASSIGNMENT---------
#114. wap to get the following output.
#s='kabab is love'
#out={'kb':('kbb',3,'bbk'),'is':('s',1,'s'),'le':('lv',2,'vl')}
'''s='kabab is love'
out={}
for i in s.split():
    count=0
    con=''
    for j in i:
        if j  not in 'AEIOUaeiou':
            count+=1
            con+=j
    out[i[0]+i[-1]]=(con,count,con[::-1])
print(out)'''

#113. wap to get the following output.
#s='kabab is love'
#out={'kb':('babak',2,'kbb'),'is':('si',1,'i'),'le':('evol',2,'lv')}
'''s='kabab is love'
out={}
for i in s.split():
    count=0
    ch=''
    for j in i:
        if j in 'AEIOUaeiou':
            count+=1
            ch+=j
    out[i[0]+i[-1]]=(i[::-1],count,i[::2])
print(out)'''

#116 wap to get the following output.
#in='bacbcaabbbaa'
#out='b4a5c2'
'''s='bacbcaabbbaa'
out=''
for i in s:
    if i not in out:
      out+=i+str(s.count(i))
print(out)'''

#119 wap to get the following output.
#in={10:'star',20:'bye',30:'moon',40:'apple'}
#out={10:'a',20:'e',30:'oo',40:'ae'}
'''d={10:'star',20:'bye',30:'moon',40:'apple'}
out={}
for k in d:  
    c=''  
    for i in d[k]: 
        if i in 'aeiou':
            c+=i      
    out[k]=c
print(out)'''
    
#wap to get the following output.
#in=[100,200,50,400,300]
#N=300
#out=[[100,200],[300]]

        
        
        
    
    
        

            
        


