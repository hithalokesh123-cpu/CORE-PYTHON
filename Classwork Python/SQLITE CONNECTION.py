# create the table
# import sqlite3
# a=sqlite3.connect('data.db')
# b=a.cursor()
# #b.execute("create table Student(rollno number,name varchar,phno number,marks number)")
# a.commit()
# a.close()


#insert the records
# import sqlite3
# a=sqlite3.connect('data.db')
# b=a.cursor()
# b.execute("insert into Student values(111,'Minchu',7894567966,65)")
# b.execute("insert into Student values(222,'Cinchu',7654345678,55)")
# b.execute("insert into Student values(333,'Dinku',6545677778,77)")
# b.execute("insert into Student values(444,'Kinku',8888777797,95)")
# b.execute("insert into Student values(555,'Jinkuu',5675859687,85)")
# a.commit()
# a.close()



#read and fetch the data
# import sqlite3
# a=sqlite3.connect('data.db')
# b=a.cursor()
# data=b.execute("select * from Student")

# fetchone()=>returns the first record
# print(list(data))
# print(data.fetchone())                            #(111, 'Minchu', 7894567966, 65)

# #fetchmany(3) => return starting 3 records
# print(data.fetchmany(3)[1][1])                      #Cinchu

# #fetchall()
# print(data.fetchall())    
# output= [(111, 'Minchu', 7894567966, 65), (222, 'Cinchu', 7654345678, 55), (333, 'Dinku', 6545677778, 77), 
#  (444, 'Kinku', 8888777797, 95), (555, 'Jinkuu', 5675859687, 85)]

# a.commit()
# a.close()
