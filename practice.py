# import sys

# import os
# info=os.system("systeminfo")
# print(info)
# import smtplib as s
# ob=s.SMTP("smtp.gmail.com",587)
# ob.starttls


# sender = 'akash.kc3745@gmail.com'
# receivers = ['aakashchhetri3745@gmail.com']

# message = """From: From Person 'akash.kc3745@gmail.com'
# To: To Person 'aakashchhetri3745@gmail.com'
# Subject: SMTP e-mail test
# This is a test e-mail message.
# """

# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)         
#    print( "Successfully sent email")
# except SMTPException:
#    print ("Error: unable to send email")

import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
# ob.starttls
ob.starttls()
ob.login("akash.kc3745@gmail.com","email password")
subject="Today is python class"
body="today is the python class for sending an email"
message="Subject:{}\n\n{}".format(subject,body)
listofaddress=["aakashchhetri3745@gmail.com","nischal.nik@gmail.com"]
ob.sendmail("akash.kc3745@gmail.com",listofaddress,message)
print("send sucessfullly")
ob.quit()














# print("This is a \"single\" line comment")
# print("This is\r jus\nt a \bpractice")

# var1=list(range(10,30,3))
# print(var1)
# var2=list(range(-1,-20,-4))
# print(var2)
# var3=list(range(10,0,-1))
# print(var3)

# passing function as argument to another function
# def secondfun():
#     return ("second function")

# def firstfun(str):
#     return(f"this is firstfunction and {str}")
# print(firstfun(secondfun())

# def addition():
#     a=20
#     b=30
#     return a+b

# def subtraction(add,value):
#     sub=add-value
#     return(sub)
# print(subtraction(addition(),30))

# # a=None
# # b=None
# # c=None
# def addition():
#     # global a,b 
#     return a+b
# a=int(input("Enter first number"))
# b=int(input("Enter first number"))

# def subtraction(add,value): 
#     # global c   
#     sub=(add-value)  
#     return(f"The addition is {add}. The subtraction is {sub}")

# c=int(input("Enter third number"))
# print(subtraction(addition(),c))

#function returning another function
# def firstfun():
#     return("This is main function")
# def secondfun():
#     print("this is sub function")
#     return firstfun()

# print(secondfun())


# def evnod(num):
#     even=[]
#     odd=[]
#     for i in num:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output=[even,odd]
#     return output
# lst=[1,2,3,4,5,6,7,8,9,10]
# print(evnod(lst))


# for i in range(0,5):
#     for j in range(i):
#         print("*", end="") 
#         for k in range(j,0,-1):
#             print("*", end="") 
#         print()












        


