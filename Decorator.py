


# def decorator_function(any_function):
#     @wraps(any_function)
#     def warpper_function(*args,**kwargs):
#         '''this is wrapper function doctype'''
#         print("he is a worls best player")
#         return any_function(*args,**kwargs)
#     return warpper_function

# @decorator_function
# def player1():
#     '''this is player one doctype'''
#     print("he is cristano ronaldo")

# player1()
# print(player1.__name__)
# print(player1.__doc__)

# @decorator_function
# def player2():
#     print("he is lionel messi" )
# player2()

# @decorator_function
# def addition(a,b):
#     return a+b
# print(addition(2,3))
def deco_func(anyfunction):
    def wrapper_func():
        anyfunction()
        print("he is a great entertainer")
    return wrapper_func

@deco_func
def player_1():
    print("cristano is best player")
@deco_func
def player2():
    print("Messi is a best player")



# var1=deco_func(player2)
# var1()

player_1() 
# player2()