# squre=[i**2 for i in range(1,11)]
# squre=[-i for i in range(1,11)]
# squre=[-i for i in range(11,1,-1)]
# print(squre)
# name=["Aakash","Biskash","Pawan","pratik"]
# wor=[name[0] for words in name]
# print(wor)

lst=[1,2,5,4,7]
revlst=[ ]

# rev=[revlst.insert(0,i) for i in lst]
rev=[revlst.append(i) for i in lst[::-1]]

print(revlst)



     

# def rev():
#     return [i for i in range(5,0,-1)]
# print(rev())

# lst=['abc','def','ghi']
# def rev(par):
#     return [i[::-1] for i in par]
# print(rev(lst))

# Even_num=[i for i in range(1,20) if  i%2==0]
# print(Even_num)
# Evennum=[True if  i%2==0 else False for i in range(1,20)]
# print(Evennum)

# newlist=['pratik',[1,2,3],1,4.0,5,10,11.5,12.6]
# def string(par):
#     nlist=[str(i) for i in par if type(i)==int or type(i)==float]
#     return nlist
# print(string(newlist))
# #nested loop:
# lister=[[i for i range(1,5)]]

