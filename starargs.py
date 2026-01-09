# def addition(num1,num2):
#     return num1+num2
# print(addition(10,15,16))


# def addition(*args):
#     print(args)
#     print(type(args))
# addition(10,15)

# def addition(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(addition(10,20,40,50,60))

# def multiplication(n1,n2,*args):  #( always start in normal parameter and args)
#     multiply=1
#     for i in args:
#         multiply*=i
#     return multiply
# print(multiplication(1,2,3,4,5))
# l=[1,2,3,4,5]
# def multiplication(n1,n2,*args):  #( always start in normal parameter and args)
#     multiply=1
#     for i in args:
#         multiply*=i
#     return multiply
# print(multiplication(*l))

# def power(n1,*args):
#     if args:
#         return[i**n1 for i in args]
#     else:
#         return "you didn't pass args"
# print(power(5,2,3,4,6,7))
# print(power(5))



#double star args **

# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# fun()

# def funct(n,**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
#     print(n)
# (funct("akash",name="sushant",age=24))

#argument giving type (normal,*args,name="default",**kwargs)


def all(*args,**kwargs):
    # print(n1)
    print(args)
    # print(profession)
    print(kwargs)
all("Aakash",20,40,"bishal",50,college="cct",faculty="technology")

# def all(n1,*args,profession="Developer",**kwargs):
#     print(n1)
#     print(*args)
#     print(profession)
#     print(kwargs)
# all("Aakash",20,40,"bishal",50,college="cct",faculty="technology")






