# class Student:
#     std_count=0
#     def __init__ (self,name,course):
#         self.name=name
#         self.course=course
#         Student.std_count+=1
#     def displaycount(self):
#         print("total student %.2f" % Student.std_count)
#     def displaystudent(self):
#         print ("name:",self.name,  "course:",self.course)
# std1=Student("aakash","python")
# std2=Student("Bikash", "php")
# std1.displaystudent()
# std2.displaycount()

# x=5
# y=x


class Person:
    def __init__(self, fullname, age, address):
        self.fullname=fullname
        self.age=age
        self.address=address

     # instance method    
    def Details(self,):
        print(f"name={self.fullname}, age={self.age}, address={self.address}")
    def fullinfo(self,):
        print(f"name={self.fullname}, age={self.age}, address={self.address}, profession={self.profession}")
    
    def sing(self,song):
        print(f"{self.fullname} {song}")
    

obj=Person("pratik", 14, "kunjalapur",)
obj1=Person("sushant", 12, "kotihawa")
# obj.sing("bazzi")
print(getattr(obj,'profession','webdeveloper'))

print(hasattr(obj,'age'))  #to check the element whether it exist on class
print(setattr(obj,'profession','Software Developer'))
# delattr(obj,'age')
# delattr(obj1,'age')
obj.Details()
obj.fullinfo()

class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def fulldetail(self):
        return(f"Student name is {self.name} and course is {self.course}")
    def fullinfo(self):
        return(f"Student name is {self.name} and course is {self.course} and address is {self.address}")

object1=Student('Nischal','BCA')
object2=Student('Pawan','python')
setattr(object1,'address','Golpark')
setattr(object2,'address','shankarnagar')

print(object1.fulldetail())
print(object2.fulldetail())
print(object1.fullinfo())
print(object2.fullinfo())









