# lst=[1,2,3,4,5,6]
# is_even=filter(lambda n:n%2==0,lst)
# for i in is_even:
#     print(i)

lst=[1,2,3,4,5,6]
is_even=filter(lambda n:True if n%2==1 else False,lst)
for i in is_even:
    print(i)



