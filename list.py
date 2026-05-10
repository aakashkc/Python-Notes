# string=["Aakash","Pawan","sushant","pratik"]

# print(string[0:4:2])

# number=[2,3,6,8,4,7,12,14,15,8,4]
# print(number[2:6:2])
# print(number[1:4])
# print([number]*3)
# number.insert(2,"this is tuple")
# print(number)
# print(number.pop())
# # number.sort()
# # var1=sorted(number)
# var2=max(number)
# var3=min(number)
# string.append("Bishal")
# string.insert(2,"Rohit")
# string[1]="Bishal"
# string.pop()
# string.remove("Aakash")
# string.remove(2)
# print(string)
# print(number)
# print(var1)
# print(var2)
# print(var3)
# print(string)


# it=iter(string)
# print(next(it))
# print(next(it))
# print(next(it))


# if "pratik" in string:
#     print("he is presrent")
# else:
#     print("he is not present")
# usinf for loop:
# for name in (string):
#     print(name)

# for name in range(len(string)):
#         print(string[name])


# usinf while loop:

# c=0
# while c<len(string):
#     print(string[c])
#     c=c+1


# print(string)
# print(string[2:4])

# Number=[1,2,3,4,5,6,7]
# print(Number)

# Mixed=["Aakash",1,2,2]

# def even_odd(num):
#         odd_num=[ ]
#         even_num=[ ]
#         for i in num:
#             if i%2==0:
#                 even_num.append(i**2)
#                 # return even_num
#             else:
#                 odd_num.append(i**2)
#                 # return odd_num

#         output=[even_num,odd_num]
#         return output
# lister=[1,2,3,4,5,6,7,8,9,10]
# print(even_odd(lister))


# def evenodd(num):
#     even=[]
#     odd=[]
#     for i in num:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output=[even,odd]
#     return output
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(evenodd(numbers))


# task 1
# def squre(num):
#     string=[]
#     for i in num:
#         print(string.append(i**2))
#     return string
# number=[1,2,3,4,5,6,7,8,9,10]
# print(squre(number))
# task 2
# listers=[1,2,3,4]
# def reverse():
#     take=[]
#     a=1
#     while a<=4:
#         take.append(listers.pop())
#         a=a+1
#     return(take)
# print(reverse())

# listers=[1,2,3,4]
# def reverse():
#     take=[]
#     for i in range(len(listers)):
#         var1=listers.pop()
#         take.append(var1)
#     return(take)
# print(reverse())


# tsk3
# string=['abc','dcf','ani','acb']
# def rev():
#     take=[]
#     for i in range(len(string)):
#         var1=string[i]
#         take.append(var1[::-1])
#     return take
# print(rev())

# task4

# def common(par1,par2):
#     newlst=[]
#     for i in range(len(par1)):
#         if par1[i] in par2:
#             newlst.append(lst1[i])
#     return newlst
# lst1=[1,2,3,7,9]
# lst2=[1,12,13,7]
# print(common(lst1,lst2))

# taks5
# lst1=[5,6,3,4,6,7,5]
# def sum1(par1):
#     sum=[]
#     add=0
#     for i in lst1:
#         add=add+i
#     sum.append(add)
#     return sum
# print(sum1(lst1))

# task#6
# list1=[1,2,3,[2,1,5,6],4,5,[7,8,9,],[5,3]]
# def counting(lst):
#     cnt=0
#     for i in lst:
#         if type(i) is type(lst):
#             cnt=cnt+1
#     return cnt
# print(counting(list1))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatlist = []
# for i in matrix:
#     flatlist.extend(i)
# print(flatlist)

# for i in matrix:
#     for j in i:
#         flatlist.append(j)
# print(flatlist)

flatlist = [j for i in matrix for j in i]
print(flatlist)
