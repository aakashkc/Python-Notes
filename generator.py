# it make our data uniterable
# generator are iterator
# l=[1,2,3,4]
# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

def number(n):
    for i in range(1,n+1):
        yield i
# for i in (number(10)):
#     print(i)
# for i in (number(10)):
#     print(i)
a=number(10)
for i in a:
    print(i)
for j in a:
    print(j)


var=yield i**3 for i in range(1,11)
print(var)


