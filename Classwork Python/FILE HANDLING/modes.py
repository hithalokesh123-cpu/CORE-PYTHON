#write()=>write,writelines
######## CREATE THE NEW FILE FIRST AND ADD THE DATA ############
'''f=open('file1.txt','w')
f.write('Hello good afternoon\n')
f.writelines(['Good afternoon mam\n','python class is started\n','we are deal with file handling concept\n'])
f.close()'''


## existing file -->overidden the data
'''f=open('file1.txt','w')
f.write('Hello good afternoon MADAM\n')
f.close()'''


#read()=>read,readline,readlines
#read()=>entire file
'''try:
   f=open('file1.txt','r')
   data=f.read()
except:
    print('file not found')
else:
    print(data)'''

#readline()=>one line at once 
'''try:
   f=open('file1.txt','r')
   data=f.readline()
except:
    print('file not found')
else:
    print(data)
    print(f.readline())
    print(f.readline())'''

#readlines()=>read all the lines in the form list 
'''try:
   f=open('file1.txt','r')
   data=f.readlines() 
except:
    print('file not found')
else:
    print(data)'''

#append => add data with existing data
'''f=open('file1.txt','a')
f.write('Python is programming languge\n')
f.close()'''

#x--> mode=> *file exist=>error  *file not exist=>create and write the data
'''f=open('file1.txt','x')
f.write('Python is programming languge\n')
f.close()'''






#*************************** ******************************** ***************************************************
#w+(write and read)
'''f=open('file1.txt','w+')
f.writelines(['\n today is boring day \n','file handling is not short\n'])
f.seek(0)        #0
print(f.read())
print(f.tell())  #59
f.close()'''


#r+(read +write)
#r+w
'''f=open('file1.txt','r+')
print(f.read())
f.write('\n core python complete\n')
f.close()'''

#output
##today is Monday 
##it is going to end the class 
##in 3 days 
##mam is planning to give backup classes also .
##
## core python complete

#w+r
'''f=open('file1.txt','r+')
f.write('Yesterday')
print(f.read())
f.close()'''

#output==>
##Monday 
##it is going to end the class 
##in 3 days 
##mam is planning to give backup classes also .
##
#### core python complete

##file ==>
##Yesterday Monday 
##it is going to end the class 
##in 3 days 
##mam is planning to give backup classes also .
##
## core python complete


#seek(index)+w+r
'''f=open('file1.txt','r+')
f.seek(0)
f.write('Today ')
print(f.read())
f.close()'''

##Today day is monday 
##it is going to end the class 
##in 3 days 
##mam is planning to give backup classes also .
##
## core python complete

#seek(index)+w+r
'''f=open('file1.txt','r+')
f.seek(13)
f.write('Tuesday ')
print(f.read())
f.close()'''

##Today day is Tuesday 
##it is going to end the class 
##in 3 days 
##mam is planning to give backup classes also .
##
## core python complete

#a+ seek() is doesn't matter data is addN AT END 
'''f=open('file1.txt','a+')
f.seek(13)
f.write('Tuesday ')
print(f.read())
f.close()'''


##Today day is Tuesday 
##it is going to end the class 
##in 3 days 
##mam is planning to give backup classes also .
##
## core python complete
##Tuesday







#************************************ ****************************************** ******************************
# rb(read binary)
'''f=open('image1.AVIF','rb')
data=f.read()
print(data)'''

# give output in decode way XXXX%&*CBMCG^&OH

#wb (write binary)
'''f=open('image1.AVIF','rb')
data=f.read()
f=open('image2.AVIF','wb')
f.write(data)
f.close()
'''

#binary--->text file
'''l=b'[1,2,3,4]'
f=open('file1.txt','wb')
f.write(l)
f.close()'''

#[1,2,3,4]


#*** pikcle concept *****
'''import pickle
l=[1,2,3,4]
data=pickle.dumps(l)  # convert original data to bytes
f=open('file1.txt','wb')
f.write(data)
print(data)
print(pickle.loads(data))  # convert bytes to original data
f.close()'''







#*******************************************************************************************
#wb+
'''f=open('file1.txt','wb+')
f.write(b'python programming language')
f.seek(0)
print(f.read())
f.close()'''


#rb+
#read=>write
'''f=open('file1.txt','rb+')
print(f.read())
f.write(b'File handling concept start')
f.close()'''
#python programming languageFile handling concept start


#write=>read
'''f=open('file1.txt','rb+')
f.seek(7)
f.write(b'Javascript ')
print(f.read())
f.close()'''
#python Javascript  languageFile handling concept start


#ab+
'''f=open('file1.txt','ab+')
f.write(b'\n it is helpful for Artificial intelligence')
print(f.read())
f.close()'''
#python Javascript  languageFile handling concept start
#it is helpful for Artificial intelligence

#pickle=> dumps
'''import pickle
data={'python':6,'java':4,'c++':3,'php':3}
c=pickle.dumps(data)
print(data,c)
f=open('file1.txt','wb+')
f.write(c)
f.close()'''
##{'python': 6, 'java': 4, 'c++': 3, 'php': 3}
##b'\x80\x04\x95)\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x06python\x94K\x06\x8c\x04java\x94K\x04\x8c\x03c++\x94K\x03\x8c\x03php\x94K\x03u.'

#pickle=>loads
'''import pickle
d={'python':6,'java':4,'c++':3,'php':3}
c=pickle.dumps(d)
print(d,c)
f=open('file1.txt','wb+')
f.write(c)
print(pickle.loads(c))
f.close()'''

#{'python': 6, 'java': 4, 'c++': 3, 'php': 3} b'\x80\x04\x95)\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x06python\x94K\x06\x8c\x04java\x94K\x04\x8c\x03c++\x94K\x03\x8c\x03php\x94K\x03u.'
#{'python': 6, 'java': 4, 'c++': 3, 'php': 3}
