# add=(lambda a,b:a*b)#(2,5)
# print(add(5,5))

# name=(lambda a:a[-1])
# print(name("akash"))


# odd_even=(lambda n:True if n%2==0 else False)(10)
# print(odd_even)
#task1

arg=(lambda *args:True if len(args)>5 else False)
print(arg(5,6.7,8,95,4,1,8))

#enumerate
names=['aakash','pawan','sushant','pratik']
for position,i in enumerate(names):
    print(f'{position} {i}')




