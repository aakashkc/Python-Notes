# class mobile:
#     def __init__(self,name,price,model):
#         self.name=name
#         self.price=price
#         self.model=model

#     def fulldetail(self):
#         return f"the detail of phone is {self.name}"
    
#     def callingfunct(self,number):
#         return f"the number of phone is {number}"

# class samsung(mobile):
    
#     def __init__(self,name,price,model,ram,camera):
#         super().__init__(name,price,model)
#         self.ram=ram
#         self.camera=camera

    

# class iphone(samsung):
#     def  __init__(self,name,price,model,ram,camera,Rom,):
#         super().__init__(name,price,model,ram,camera)
#         self.Rom=Rom

# obj=mobile("Nokia",5000, 1100)
# obj1=samsung("Nokia",5000, 1100,"15gb","20mp")
# obj2=iphone("Nokia",5000, 1100,"15gb","20mp","10")
# print(obj.callingfunct(9568452))


class Parent: # define parent class
	parentAttr = 100 
	def __init__(self): 
		print ("Calling parent constructor") 
	def parentMethod(self): 
		print ('Calling parent method') 
	def setAttr(self, attr): 
		Parent.parentAttr = attr 
	def getAttr(self): 
		print ("Parent attribute :", Parent.parentAttr) 


class Child(Parent): # define child class 
	def __init__(self): 
		print ("Calling child constructor") 
	def childMethod(self): 
		print ('Calling child method') 
    def parentMethod(self): 
		print ("Calling parent method") 
    
    
  

c = Child() # instance of child 
c.childMethod() # child calls its method 
c.parentMethod() # calls parent's method 
c.setAttr(200) # again call parent's method 
c.getAttr() # again call parent's method 
# c.parentMethod()



        
    

        