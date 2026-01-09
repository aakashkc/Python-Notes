# def power(number):
    # return number**2
lst=[1,2,3,4,5]
# new=map(power,lst)
# for i in new:
#     print(i)

new=map((lambda l:l**3),lst)
for i in new:
    print(i)




