

#Q=5
# name=input("Enter a name")
# age=int(input("Enter a age"))
# # firstletter=name[0].upper()
# if age>=18 and (name[0].upper()) == "A":
#     print("You are Eligible for vote")
# else:
#     print("You are not Eligible for vote")





#Q=6: using for loop
# number=int(input("enter a number"))
# count=0
# for i in range((number)+1):
#     count=count+i
# print(count)

#using while loop:
# number=int(input("enter a number"))
# count=1
# total=0

# while count<=(number):
#     total=total+count
#     count=count+1
# print(total)










#Q=7
# number=input("Enter a number")
# count=0
# for i in number:
#     count=count+int(i)
# print(count)

#Q=8

name=input("Enter a name")
var1=" "
for i in name:
    if i not in var1:
        var1=var1+i    
        var2=name.count(i)
        print(f"{i}:{var2}")

#Q=9
# var1=int(input("Enter a number"))
# var2=int(input("Enter a second number"))
# def greatest(par1,par2):
#     if par1>par2:
#         print(f"greatest is {par1}")
#     else:
#         print(f"greatst is {par2}")
# greatest(var1,var2)

#Q=10:
# string=input("Enter a string")
# def palindrome(par1):
#     if par1==par1[::-1]:
#         return True
#     else:
#         return False
# print(palindrome(string))

#q=11
# list1=[1,2,3,4,5]
# list2=[]
# def squre(para1):
#     for i in list1:
#         list2.append(i**2)
#     return list2
# print(squre(list1))

#Q12:
# list1=[1,2,3,4,5]
# list2=[]
# def reverse(par1):
#     for i in range(len(par1)):
#         list2.append(par1.pop())
#     return list2
# print(reverse(list1))


#Q13:
# list1=['abc','def','ghi']
# list2=[]
# def reverse(para1):
#     for i in para1:
#         var1=i[::-1]
#         list2.append(var1)
#     return list2
# print(reverse(list1))

#Q14
# list1=[1,2,3,4,5,6,7,8,9]
# odd=[]
# even=[]
# def odd_even(par1):
#     for i in list1:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output=[odd,even]
#     return output
# print(odd_even(list1))

#q15:
# list1=[1,2,3,6,7,8]
# list2=[1,5,8,9,2,8]
# same=[]
# def common(par1,par2):
#     for i in par1:
#         if i in par2:
#             same.append(i)
#     return same
# print(common(list1,list2))

#Q=16:
# list1=[4,5,[5,6],[],[2],[5,4],4,3]

# def listcount(par1):
#     count=0
#     for i in par1:
#         if type(i)==type(par1):
#             count+=1
#     return count
# print(listcount(list1))


# calculation=lambda a,b:a*b
# print(calculation(5,6))

# user=lambda:"this is string"
# print(user())
# print(user())
# print(user())

# filtermethod

# ages=[13,90,17,59,21,60,5]
# adults=list(filter(lambda age:age>18,ages))
# print(adults,end=" ")

# i=1
# while i<=10:
#     print(i,end=",")
#     i+=1

# 1
# 12
# 123
# 1234
# 12345
# total=""
# for i in range(1,6):
#     total=total+str(i)
#     print(total)

# num=int(input("enter a number"))
# def ptrn(number):
#     for i in range(number+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# ptrn(num)
# 1,2,3,5,7,11

# x=2
# for i in range(x):
#     x+=1
#     print(x)
total=""
def has():
    for i in range(6):
        for j in range(i):
            print("*",end=" ")
        print()
has()


    




    














# num=int(input("enter a number"))
# def ptrn(number):
#     for i in range(number+1):
#         for j in range(1,i+1):
#             print(i,end=" ")
#         print()
# ptrn(num)



# 11235













        








