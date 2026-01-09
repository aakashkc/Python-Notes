# Age=int(input("Enter age of person"))
# if int(Age)==0 or int(Age)<0:
#     print("Your are alien")
# elif 0<Age<3:
#     print("Your ticket price is Rs10")
# elif 3<Age<10:
#     print("Your ticket price is 20")
# elif 10<Age<20:
#     print("Your Ticket price is 30")
# elif 20<Age<50:
#     print("Your ticket price is 100")

A,B,C=input("Enter a Number").split(",")
if int(A)>int(B) and int(A)>int(C) :
    print("The Greatest is a")
elif int(B)>int(A) and int(B)>int(C):
    print("The Greatest is b")

elif int(A)==int(B)==int(C):
    print("They are equal")
else:
    print("The Greatest is c")



    
