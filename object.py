#class object method
# class person:
#     def __init__(self,firstname,lastname,age):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age

# firstperson=person('pratik','gadhal',23)
# secondperson=person('sushant','thakuri',23)
# print(f"{firstperson.firstname} {firstperson.lastname} {firstperson.age}")
# print(f'{secondperson.firstname} {secondperson.lastname} {secondperson.age}')


# # 1st way
# disc=0
# class mobile:
#     discountpercent=10
#     vatpercent=10 
#     def __init__(self,mobilename,model,price):
#         self.mobilename=mobilename
#         self.model=model
#         self.price=price
#     def full_detail(self):
        # return (f"{self.mobilename} {self.model} {self.price}")
#     def apply_discount(self): 
#         discount_amount=(mobile.discountpercent/100*self.price)
#         global disc
#         disc=self.price-discount_amount 
#         return disc
#     def vat(self):
#         x=disc
#         return mobile.vatpercent/100*x+disc

# mobileobject=mobile("samsung galaxy","s9",20000)
# print(f"Amount after {mobileobject.discountpercent} percent discount is {mobileobject.full_detail()}")
# print(mobileobject.apply_discount())
# print(mobileobject.vat())

# 2nd way
class mobile:
    discountpercent=10
    vatpercent=13 
    def __init__(self,mobilename,model,price):
        self.mobilename=mobilename
        self.model=model
        self.price=price
        self.disc=None
    def full_detail(self):
        return (f"{self.mobilename} {self.model} {self.price}")
    def apply_discount(self): 
        discount_amount=(mobile.discountpercent/100*self.price)
        self.disc=self.price-discount_amount 
        return self.disc
    def vat(self):
        x=self.disc
        return mobile.vatpercent/100*x+self.disc
mobileobject=mobile("samsung galaxy","s9",20000)
print(f"Amount after {mobileobject.discountpercent} percent discount is {mobileobject.full_detail()}")
print(mobileobject.apply_discount())
print(mobileobject.vat())

# disc=0
# class mobile:
#     discountpercent=10
#     vatpercent=13 
#     def __init__(self,mobilename,model,price):
#         self.mobilename=mobilename
#         self.model=model
#         self.price=price
#     def full_detail(self):
#         return (f"{self.mobilename} {self.model} {self.price}")
#     def apply_discount(self): 
#         discount_amount=(mobile.discountpercent/100*self.price)
#         global disc
#         disc=self.price-discount_amount 
#         return disc
#     def vat(self):
#         x=disc
#         return mobile.vatpercent/100*x+disc

# mobileobject=mobile("samsung galaxy","s9",20000)
# print(f"Amount after {mobileobject.discountpercent} percent discount is {mobileobject.full_detail()}")
# print(mobileobject.apply_discount())
# print(mobileobject.vat())





# class Employee:
#     #init method also called a constructor
#     def __init__(self,Emp_name,address,salary):
#         #instance or object variable
#         self.name=Emp_name
#         self.address=address
#         self.salary=salary
# #creating object of class
# objname=Employee('Aakash','kc',25000)
# objname2=Employee('Bisal','kc',30000)

# print(objname.name)
# print(objname2.name)

# class Laptop:
#     def __init__(self,Brandname,modelname,price):
#         self.Brandname=Brandname
#         self.modelname=modelname
#         self.price=price
#         self.fulldetail=Brandname+' '+modelname
        
#     def detail(self):
#         return f"{self.Brandname} {self.modelname} {self.price}"  #can only concatinate string not intiger
    
#     def cando(self):
#         return self.price>20000
# object1=Laptop('toshiba',"12545",50000)
# print(f"{object1.Brandname},{object1.modelname}")
# print(object1.fulldetail)
# print(object1.detail())
# print(object1.cando())

        
# class circle:
#     py=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def circumfrence (self):
#         return 2*circle.py*self.radius**2
# newobj=circle(10)
# obj1=circle(20)
# print(newobj.circumfrence())
# print(obj1.circumfrence())




# mobileobject.discount=50//100