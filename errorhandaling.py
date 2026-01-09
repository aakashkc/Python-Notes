# def fun1(a,b):
#     #if type(a)== type(b)== int
#     if type(a) is int and type(b) is int: 
#         return (a+b)
#     raise ValueError("your values cannot be operated")
# print(fun1(12,'12'))
# # while True:
#     try:
#         age=int(input("enter your age"))
#         break
#     except ValueError:
#         print("you input is invalid")
# if age>=18:
#     print('you are able to vote')
# else:
#     print('you are not able to vote')


# num1=input('enter a first number')
# num2=input('enter a second number')
# try:
#     num3=num1-num2
#     c=int(num1)-int(num2)
# except TypeError:
#     print("this throws an type error")
# except ZeroDivisionError as obj:
#     print(obj)
# except TypeError:
#     print('you cannot do operation with recently input values')
# except ValueError:
#     print('your entered value throw value error')
# # except NameError as thisname:
# #     print(f'this throws an nameError{thisname}')
# except:
#     print('Some Exception is occured in your program')

# else:
#     print(num3)
#     print(c)
# def addition(a,b):
#     if type(a) is int and type(b) is int:
#         return (a+b)
#     raise ValueError("this is an error argument passed")
# print(addition(10,20))

a=int(input("enter anumber"))
if a>100:
    raise ValueError("your input is beyound consideration")
else:
    print("you entered correct number")



