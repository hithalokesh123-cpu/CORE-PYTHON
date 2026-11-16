#*************************** CSV *******************************
#********** w(write) ************
'''import csv
f=open('exam.csv','w')
ob=csv.writer(f)
ob.writerow(['Rollno','Name','Contactno','Marks'])
ob.writerows([[101,'Pinky',333355558,95],[102,'Dimpu',7777888890,75],[103,'Jinku',9999567444,50],[104,'Kukoo',7878787890,25]])
f.close()'''

#******** r(read) *******************
#-------- with[] space is added using for loop -------------
'''import csv
f=open('exam.csv','r')
ob=csv.reader(f)
for i in ob:
        print(i)'''

#output
##['Rollno', 'Name', 'Contactno', 'Marks']
##[]
##['101', 'Pinky', '333355558', '95']
##[]
##['102', 'Dimpu', '7777888890', '75']
##[]
##['103', 'Jinku', '9999567444', '50']
##[]
##['104', 'Kukoo', '7878787890', '25']
##[]


#----------- remove space using logic if cond ---------------
'''import csv
f=open('exam.csv','r')
ob=csv.reader(f)
for i in ob:
    if i!=[]:
        print(i)'''

#output
##['Rollno', 'Name', 'Contactno', 'Marks']
##['101', 'Pinky', '333355558', '95']
##['102', 'Dimpu', '7777888890', '75']
##['103', 'Jinku', '9999567444', '50']
##['104', 'Kukoo', '7878787890', '25']

#-------- while writing only add newline() -------------------------
'''import csv
f=open('exam.csv','w',newline='')
ob=csv.writer(f)
ob.writerow(['Rollno','Name','Contactno','Marks'])
ob.writerows([[101,'Pinky',333355558,95],[102,'Dimpu',7777888890,75],[103,'Jinku',9999567444,50],[104,'Kukoo',7878787890,25]])
f.close()'''

#output
##Rollno,Name,Contactno,Marks
##101,Pinky,333355558,95
##102,Dimpu,7777888890,75
##103,Jinku,9999567444,50
##104,Kukoo,7878787890,25


#append the new data
'''import csv
f=open('exam.csv','a')
ob=csv.writer(f)
ob.writerow([105,'Oggy',8989809876,85])
f.close()'''

#****************** without close() the file *******************
#----------------- Context manager -----------------------------
import csv
with open('exam.csv','a')as f:
    ob=csv.writer(f)
    ob.writerow([106,'bheem',7676547754,70])
