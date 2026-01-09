#user define function
# def addition (x,y):
#     return x+y
# print(addition(4,5))


# def add(Firstname,Lastname):
#     return Firstname+Lastname
# fn=input("Enter a first name")
# ln=input("Entera a last name")  
# print(fn,ln)

# def odd_even(num):
#     return num%2==0
#         # return "The number is even"
# #         return True
# #   # else:
# #     # return "The number is odd"
# #     return False
# print(odd_even(10))
#1st way
# def name(lname):
#     return lname[-1]
# value=input("Enter a name")
# print(name(value))
# second way
# def fname(name):
#     return name[len(name)-1]
# var1=input("Enter a name")
# print(fname(var1))


# def sum (a,b):
#     # a=20
#     b=20
#     return (a+b)
# a=10
# print(sum(a,1))

# task 1
# def palindrome(character):
#     revcharacter=string[::-1]
#     if character==revcharacter:
#         return True
#     else:
#         return False
# string=input("Enter a string")
# print(palindrome(string))

#task2
# num1=int(input("Enter a first number"))
# num2=int(input("Enter a second number"))
# def greatest(num1,num2):
#     if num1>num2:
#         return f"the greatest is{num1}"
#     else:
#         if num1==num2:
#             return (f"both are equal")
#         else:
#             return "the smallest is",num2
# print(greatest(num1,num2))

# no1=int(input("Enter a first number"))
# no2=int(input("Enter a second number"))
# no3=int(input("Enter a three number"))
# def small_great_equal(num1,num2,num3):
#     if (num1>num2) and (num1>num3) and (num2!=num3):
#         return (f"greates is {num1}")
#     elif (num2>num3) and (num2>num1) and (num1!=num3):
#         return (f"greatest is {num2}")
#     elif num1==num2==num3:
#         return ("All  number are equal")
#     elif (num1==num2) and (num3!=(num1==num2)):
#         return(f"{num1} and {num2} are equal")
#     elif (num2==num3) and (num1!=(num2==num3)):
#         return(f"{num2} and {num3} are equal")
#     elif (num3==num1) and (num2!=(num3==num1)):
#         return (f"{num3} and {num1} are equal")
#     else:
#         return (f"greatest is {num3}")
# print(small_great_equal(no1,no2,no3))






  

# def first_fun (a,b):
#     if a>b:
#         return a
#     else:
#         return b

# def Second_fun(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# def third_fun(a,b,c):
#     bigger=first_fun(a,b)
#     return first_fun(bigger,c)

# print(third_fun(10,20,90))

# def info_user(firstname="Aakash",lastname="chhetri",age=28):
#     print(f"My name is {firstname}")
#     print(f"My name is {lastname}")
#     print(f"My age is {age}")

# info_user()
# x=5
# def find():
#     global x
#     x=7
#     return x
# print(x)
# print(find())




#task 1
# name=input("Enter a name")
# print(f"the name is {(name.upper())}")
# print(f"the length of name is {len(name)}")

# def Name(nam):
#     length=len(string)
#     return f"the name is {string.upper()} and length of name is{length}"
# string=input("Enter a name")
# print(Name(string))


# age 1-3 no discount
#3-10 5% discount
# 10-20 3%
# 20-50 1%
# 50-90 no discount
# 90 dead
# -1 alien 
# year=int(input("Enter age"))
# def discount(age): 
#     if age<3 and age>=1:
#         return f"you are not allow to get discount"
#     elif age>=3 and age<10:
#         return f"you have  5% discount"
#     elif age>=10 and age<20:
#         return f"you have 3% discount"
#     elif age>=20 and age<50:
#         return f"you have 1% discount"
#     elif age>=50 and age<90:
#         return f"you have no discount"
#     elif age>=90:
#         return f"you are dead"
#     else:
#         return "your are alien"

# print(discount(year))



# def calculation (x,y):
#     sum=x+y
#     sub=x-y
#     return f"{sum} and {sub}"
# print(calculation(5,10))


#Nested function

# def dis(fname,lname):
#     # return "outer function" function return should be in last after block of statement
#     def show():
#         return (f"inner function {fname} {lname}")
#     print(show())
#     return(f"this is outermost function")
#     # return "outer function"

# print(dis("Aakash","chhetri"))
# global and local variable
# def outer():
#     print(f"I'm the outer function.")
#     def inner():      
#         x=5
#         y=10
#         print("And I'm the inner function.")
#         return x+y
#     print(inner())
# outer()

#global and local variable

# x="THis is string"
# def globe():
#     x=x*2
#     return ()
# print(globe())

#function returning another function
def disp():
    def show():
        return "show function"
    print("this is disp function")
    return show()
print(disp())



# eg=1
# def first_fun():
#     print(f"this is first function")

# def second_fun():
#     return first_fun()
# second_fun()


#passing function as a parameter
# eg=2
# def addition():
#     a=20
#     b=30
#     return a+b

# def subtraction(add,value):
#     sub=add-value
#     return(sub)
# print(subtraction(addition(),30))

# eg=3
# a=None
# b=None
# c=None
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



























    













    









