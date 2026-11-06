#----------pattern programming-------------------------
#   * * * 
#   * * * 
#   * * * 

'''for i in range(1,4):
    for j in range(1,4):
        print('*',end=' ')
    print()'''


#   *         
#     *       
#       *     
#         *   
#           *

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


#*         
#* *       
#* * *     
#* * * *   
#* * * * *

'''for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#* * * * * 
#  * * * * 
#    * * * 
#      * * 
#        *

'''for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''



#            * 
#          *   
#        *     
#      *       
#    *         
#  *           
#*             
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


              
#            * 
#          * * 
#        * * * 
#      * * * * 
#    * * * * * 
#  * * * * * * 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#* * * * * *   
#* * * * *     
#* * * *       
#* * *         
#* *           
#*       
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

##1         
##1 2       
##1 2 3     
##1 2 3 4   
##1 2 3 4 5

'''for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()'''

##1 1 1 1 1 
##  2 2 2 2 
##    3 3 3 
##      4 4 
##        5 
'''for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()'''
            
##A B C D   
##E F G     
##H I       
##J   
'''n=int(input('enter a number:'))
ch=ord('A')
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()'''

##A B C D E 
##A B C D   
##A B C     
##A B       
##A         
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    ch=ord('A')
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()'''

##* * * * * * * 
##*           * 
##*           * 
##*           * 
##*           * 
##*           * 
##* * * * * * * 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

## * * * * * * * 
## *     *     * 
## *     *     * 
## * * * * * * * 
## *     *     * 
## *     *     * 
## * * * * * * *             
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
         if i==1 or i==n or j==1 or j==n or i==(n//2)+1 or j==(n//2)+1:
             print('*',end=' ')
         else:
             print(' ',end=' ')
    print()'''

##* * * * * * * 
##*           * 
##*           * 
##*     *     * 
##*           * 
##*           * 
##* * * * * * *              
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
         if i==1 or i==n or j==1 or j==n  or (i==n//2+1 and i==j):
             print('*',end=' ')
         else:
             print(' ',end=' ')
    print()'''

##*           * 
##  *       *   
##    *   *     
##      *       
##    *   *     
##  *       *   
##*           * 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
           print('*',end=' ')
        else:
             print(' ',end=' ')
    print() '''

##1             
##1 4           
##1 4 3         
##1 4 3 16       
##1 4 3 16 5     
##1 4 3 16 5 36   
##1 4 3 16 5 36 7 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j :
            if j%2!=0:
               print(j,end=' ')
            else:
                print(j**2,end=' ')
        else:
             print(' ',end=' ')
    print()  '''   

##          *           
##        *   *         
##      *       *       
##    *           *     
##  *               *   
##* * * * * * * * * * * 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,(n*2)):
        if i==n or i+j==n+1 or j-i==n-1: 
             print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##      * 
##     * * 
##    *   * 
##   *     * 
##  *       * 
## *         * 
##*           * 
## *         * 
##  *       * 
##   *     * 
##    *   * 
##     * * 
##      * 
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(n-i):
         print(' ',end='')
    for k in range(i):
        if k==0 or k==i-1:
            print('* ',end='')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n):
   for j in range(i):
        print(' ',end='')
   for k in range(n-i):
       if k==0 or k==n-i-1:
            print('* ',end='')
       else:
            print(' ',end=' ')
   print()


##    * 
##   * * 
##  * * * 
## * * * * 
##* * * * * 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()'''

#OR
'''for i in range(1,n+1):
    print(' '*(n-i)+'* '*(i)'''

##     * 
##    * * 
##   * * * 
##  * * * * 
## * * * * * 
##* * * * * * 
## * * * * * 
##  * * * * 
##   * * * 
##    * * 
##     * 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()   
for i in range(1,n):
    for s in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('* ',end='')
    print()'''


#OR
'''for i in range(1,n+1):
    print(' '*(n-i)+'* '*(i)
for i in range(1,n):
    print(' '*(i)+'* '*(n-i)'''

##        5 1         
##      4 5 2 2       
##    3 4 5 3 3 3     
##  2 3 4 5 4 4 4 4   
##1 2 3 4 5 5 5 5 5 5 
##A A A A A A B C D E 
##  B B B B B C D E   
##    C C C C D E     
##      D D D E       
##        E E  

##        5 
##      4 5 
##    3 4 5 
##  2 3 4 5 
##1 2 3 4 5 

'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print() '''

##1         
##2 2       
##3 3 3     
##4 4 4 4   
##5 5 5 5 5 

'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()''' 

 
##A B C D E 
##  A B C D 
##    A B C 
##      A B 
##        A 
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    ch=ord('A')
    for j in range(1,n+1):
        if i<=j:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()'''

##A B C D E 
##B C D E   
##C D E     
##D E       
##E  
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    ch=ord('A')+i-1
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()'''

# 2 integration

'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print(j,end=' ')
        else:
            print(' ',end=' ')
   

    for j in range(1,n+1):
         if i>=j:
            print(i,end=' ')
         else:
            print(' ',end=' ')
    print()


#2 integration

for i in range(1,n+1):
    ch=ord('A')
    for j in range(1,n+1):
        if i<=j:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')

        ch=ord('A')+i-1
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()'''




##         -----------ASSIGNMENT-------------------------
#alphabet A to Z
##   * * *   
## *       * 
## * * * * * 
## *       * 
## *       * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (j==1 and i!=1) or (i==1 and 1<j<n) or (j==n and i!=1) or i==n//2+1  :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''
        


## * * * *   
## *       * 
## *       * 
## * * * *   
## *       * 
## *       * 
## * * * * 
'''for i in range (1,8):
    for j in range(1,6):
        if j==1 or (i==1 and j!=5)  or (i==4 and j!=5) or (i==7 and j!=5) or (j==5 and i!=1 and i!=4 and i!=7):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


    
##  * * * * * 
##  *         
##  *         
##  *         
##  * * * * * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##  * * * *   
##  *       * 
##  *       * 
##  *       * 
##  * * * *  
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or (i==1 and j!=n) or (j==n and i!=1 and i!=5) or (i==n and j!=5):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##  * * * * * 
##  *         
##  * * * * * 
##  *         
##  * * * * * 

'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 or i==n//2+1 or i==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



## * * * * * 
## *         
## * * * * * 
## *         
## *

'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 or i==n//2+1 :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##    * * *   
##  *         
##  *   * * * 
##  *       * 
##    * * * * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (j==1 and i!=1 and i!=n) or (i==1 and j!=n and j!=1) or (i==n and j!=n and j!=1) or (j==n and i>=n//2+1) or (i==n//2+1 and j!=2):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## *       * 
## *       * 
## * * * * * 
## *       * 
## *       * 


'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n//2+1 or j==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


##  * * * * * 
##      *     
##      *     
##      *     
##  * * * * * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n//2+1 or i==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##  * * * * * 
##      *     
##      *     
##      *     
##  * * *  
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n//2+1 or (i==5 and j<=n//2+1) :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



## *     *   
## *   *     
## * *       
## *   *     
## *     *  
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i+j==n or i-j==1:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



## *         
## *         
## *         
## *         
## * * * * * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## *       * 
## * *   * * 
## *   *   * 
## *       * 
## *       * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or (i==j and j<=3) or  (i+j==n+1 and j!=2)  or j==5 :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## *       * 
## * *     * 
## *   *   * 
## *     * * 
## *       * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==j or j==5 :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


##   * * *   
## *       * 
## *       * 
## *       * 
##   * * *  
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (j==n and 1<i<n)  or (i==n and 1<j<n) or (j==1 and 1<i<n):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

##  * * * * * 
##  *       * 
##  * * * * * 
##  *         
##  *   

'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 or i==n//2+1 or (j==5 and i<n//2+1):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##    * * *   
##  *       * 
##  *   *   * 
##  *     * * 
##    * * * * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (i==1 and 1<j<n) or (j==n and 1<i<n)  or (i==n and 1<j<n) or (j==1 and 1<i<n) or (i==j and j!=1 and j!=2):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



## * * * * * 
## *       * 
## * * * * * 
## *     *   
## *       * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 or i==n//2+1 or (j==5 and i<n//2+1) or (i==j and j!=2 and j!=1):
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



## * * * * * 
## *         
## * * * * * 
##         * 
## * * * * *
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==1 or (j==1 and i!=4 and i!=n) or i==n//2+1 or (j==n and i!=1 and i!=2) or i==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



##  * * * * * 
##      *     
##      *     
##      *     
##      * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n//2+1:
             print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



## *       * 
## *       * 
## *       * 
## *       * 
##   * * *   
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (j==1  and i!=n) or (i==n and j!=n and j!=1) or (j==n and i!=n):
             print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## *       * 
## *       * 
## *       * 
##   *   *   
##     *     
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (j==1 and i!=4 and i!=5) or (j==5 and i!=4 and i!=5) or i-j==2 or i+j==n+3:
             print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## *       * 
## *       * 
## *   *   * 
## * *   * * 
## *       * 

'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or (i+j==n+1 and 2<i<n) or (i==j and 2<j<n)  or j==5 :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## *       * 
##   *   *   
##     *     
##   *   *   
## *       * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
             print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

## *       * 
##   *   *   
##     *     
##   *       
## *  
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if (i==j and j!=4 and j!=5) or i+j==n+1 :
             print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


## * * * * * 
##       *   
##     *     
##   *       
## * * * * * 
'''n=int(input('enter:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        if i==1 or i+j==n+1 or i==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''
