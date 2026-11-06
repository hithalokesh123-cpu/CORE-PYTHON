################ COMPREHENSION ###################
 ############### LIST COMPREHENSION
'''nums=[num for num in range(1,11)]
print(nums)'''

#wap to extract only the str which start with a
'''l=['am','papu','anu']
l=[ch for ch in l if ch[0] == 'a']
print(l)'''

#wap to replace negative number with 0
'''l=[5,-9,2,3,-8,-4]
l=[0 if i<0 else i for i in l]
print(l)'''

#wap to create list that contains len of words present in the input list
'''l=['a','mango','all','be']
l=[len(word) for word in l]
print(l)'''

'''l1=[1,2]
l2=[3,4]
print([(i,j) for i in l1 for j in l2])'''
#[(1, 3), (1, 4), (2, 3), (2, 4)]

'''l1=[1,2]
l2=[3,4]
print([(i+j) for i in l1 for j in l2])'''
#[4, 5, 5, 6]

#create a list of add number from 1 to 50
'''odd_nums=[num for num in range(1,51) if num%2!=0]
print(odd_nums)'''

##################### SET COMPREHENSION ##########################
'''s='donkey'
print({(ord(i)) for i in s})'''

'''s='donkey'
print({(i,s[i]) for i in range(0,len(s))})'''
#{(4, 'e'), (5, 'y'), (0, 'd'), (2, 'n'), (1, 'o'), (3, 'k')}

'''s='donkey'
print({(i,j) for i,j in enumerate(s)})'''
#{(0, 'd'), (4, 'e'), (5, 'y'), (3, 'k'), (2, 'n'), (1, 'o')}

############## dict comprehension ####################
'''l=['apple','heaven','world','army','animal','air','pink']
#word:len(word)
l={word:len(word) for word in l}
print(l)'''
#{'apple': 5, 'heaven': 6, 'world': 5, 'army': 4, 'animal': 6, 'air': 3, 'pink': 4}

'''s='heaven'
l={ch:ord(ch) for ch in s if ord(ch)%2 == 0}
print(l)'''
#{'h': 104, 'v': 118, 'n': 110}

'''l=[1,2,3]
l2=[4,5,6]
l={i:j for i,j in zip(l,l2)}
print(l)'''
#{(2, 5), (1, 4), (3, 6)}

'''l1=[23,4.5,'hii',[1,2,3],100]
l2=[5,10,15,20,[1,2,3]]
print({i:j for i,j in zip(l1,l2) if type(i) not in [list,set,dict]})'''
#{23: 5, 4.5: 10, 'hii': 15, 100: [1, 2, 3]}

'''l=['hii','dad','mom','pink','cherry']
print({ word:len(word) if word == word[::-1] else word[::-1] for word in l})'''
#{'hii': 'iih', 'dad': 3, 'mom': 3, 'pink': 'knip', 'cherry': 'yrrehc'}


###################### ITERATOR #####################
'''l=[1,2,3]
a=iter(l)
print(next(a))
print(next(a))
print(next(a))'''

################## GENERATOR ########################
#1)
'''def sam():
    a=20
    b=30
    return a+b
    return a-b
    return a*b
print(sam())'''
#50

'''def sam():
    a=20
    b=30
    yield a+b
    yield a-b
    yield a*b'''
#using type cast to list 
'''print(list(sam())'''
#[50, -10, 600]

#using iter()
'''i=iter(sam())
print(next(i))
print(next(i))
print(next(i))
print(next(i))'''
##50
##-10
##600
#StopIteration

#2)      
def sam():
    a=20
    b=30
    print('hello good morning')
    yield a+b
    print('python is not a simplest language')
    yield a-b
    print('generator is one of the concept')
    yield a*b
    
'''print(list(sam()))'''
 
 #output   
#hello good morning
#python is not a simplest language
#generator is one of the concept
#[50, -10, 600]

'''i=iter(sam())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))'''

#output
#hello good morning
#50
#python is not a simplest language
#-10
#generator is one of the concept
#600
#StopIteration

'''def even_nums(l):
    for i in l:
        if i%2 == 0:
            yield i
print(list(even_nums([1,2,3,4,5,6,7,8,9])))'''
#[2, 4, 6, 8]

################ GENERATOR EXPRESSION ######################
'''import sys
gen=(i for i in range(1,500))
com=[i for i in range(1,500)]
print(sys.getsizeof(gen))
print(sys.getsizeof(com))'''
#output
#104
#4216

'''gen=(i for i in range(1,20))
print(list(gen))'''
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


