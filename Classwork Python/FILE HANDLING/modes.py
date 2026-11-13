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
try:
   f=open('file1.txt','r')
   data=f.readlines() 
except:
    print('file not found')
else:
    print(data)
