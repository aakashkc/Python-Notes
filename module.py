



# first create a .py extension file in which we save our python code
# for example we create a file name is addition.py that contain addition code 
 
#1) using modle

#1) we create a module .and use it using import statement we will call it to another pythonfile
#again to implement that addition.py  file module ,we will create my.py and call addition.py inside this python file

#2)Naming Module
#we can change module name as our requirement using as keyword

#3) there are several built-in module .we can import them as our requirement
# 
import platform
a=platform.system() #this give name of  which  os you are using
print(a)
# if you want to show all list of function in a module  then we use dir() function
# this shows all functions and its variable

import addition
x=dir(addition)
print(x)


import math
y=dir(math)
print(y)


