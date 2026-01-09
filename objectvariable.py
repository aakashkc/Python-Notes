# class circle:
#     py=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def circumfrence (self):
#         return 2*circle.py*self.radius**2
# newobj=circle(10)
# obj1=circle(20)
# # print(newobj.circumfrence())
# # print(obj1.circumfrence())


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
#         return (f"{self.mobilename} {self.model} {self.price}")
#     def apply_discount(self): 
#         discount_amount=(mobile.discountpercent/100*self.price)
#         global disc
#         disc=self.price-discount_amount 
#         return disc
#     def vat(self):
#         return mobile.vatpercent/100*disc+disc

# mobileobject=mobile("samsung galaxy","s9",20000)
# print(f"Amount after {mobileobject.discountpercent} percent discount is {mobileobject.full_detail()}")
# print(mobileobject.apply_discount())
# print(mobileobject.vat())

# 2nd way
# class mobile:
#     discountpercent=10
#     vatpercent=13 
#     def __init__(self,mobilename,model,price):
#         self.mobilename=mobilename
#         self.model=model
#         self.price=price
#         self.disc=None
#     def full_detail(self):
#         return (f"{self.mobilename} {self.model} {self.price}")
#     def apply_discount(self): 
#         discount_amount=(mobile.discountpercent/100*self.price)
#         self.disc=self.price-discount_amount 
#         return self.disc
#     def vat(self):
#         x=self.disc
#         return mobile.vatpercent/100*x+self.disc
# mobileobject=mobile("samsung galaxy","s9",20000)
# print(f"Amount after {mobileobject.discountpercent} percent discount is {mobileobject.full_detail()}")
# print(mobileobject.apply_discount())
# print(mobileobject.vat())


# class mobile:
#     discount=10/100
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def disamount(self):
#         return self.price-(self.discount*self.price)
# mobileobject=mobile('mI' ,30000)
# mobileobject2=mobile('samsung',20000)
# mobileobject3=mobile('IPhone',80000)
# mobileobject.discount=50/100
# # print(mobileobject.disamount())
# # print(mobileobject2.disamount())
# # print(mobileobject3.disamount())
# print(f"MI Rs {mobileobject.price}\nafter 50% discount is rs{mobileobject.disamount()}")
# print(f"Samsung Rs {mobileobject2.price}\nafter 10 % discount is {mobileobject2.disamount()}")
# print(f'IPhone Rs {mobileobject3.price}\nafter 10% discount is{mobileobject3.disamount()}')


class person:
    count=0
    def __init__(self,firstname,lastname,age):
        person.count += 1

        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    @classmethod
    def count_instances(cls):
        return f"the instance is {cls.count}"
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    def old(self):
        if self.age>=18:
            return "you are eligibke to vote"

personobject=person("Aakash","KC", 23)
personobject1=person("BIshal","pandey", 23)
personobject2=person("sagar","malla" ,23)
personobject3=person("sagar","malla" ,23)
personobject4=person("sagar","malla" ,23)
personobject5=person("sagar","malla" ,23)
personobject6=person("sagar","malla" ,23)
personobject7=person("sagar","malla" ,23)
# personobject3=person("pawan","pandey", 23)

print(person.count_instances())


