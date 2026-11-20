data='''employee mail 4567876587 id is pallavi@gmail.com  9876893456
 TYP23456 yashwanth123@gmail.COM PENT456 ashwini.k@pqr.in 9998455678 12-09-2026 12.02.26 13/04/2024'''

#phno
# pattern=r'[6-9]\d{9}'
# import re  
# phno=re.findall(pattern,data)
# print(phno)                        

# #empid
# pattern=r'[A-Z]{3,5}\d+'
# import re  
# empid=re.findall(pattern,data)
# print(empid)  

# #date
# pattern=r'[0-9]{2}[./-]+[0-9]{2}[./-]+[0-9]{2,4}'
# import re  
# date=re.findall(pattern,data)
# print(date)

# #email
# pattern=r'[a-z]+.?\d*[a-z]*\@[a-z]+.[a-z]{2,3}'
# import re  
# email=re.findall(pattern,data)
# print(email)

#output
['9876893456', '9998455678']
['TYP23456', 'PENT456']
['12-09-2026', '12.02.26', '13/04/2024']
['idis pallavi@gmail.com', 'yashwanth123@gmail', 'ashwini.k@pqr.in']