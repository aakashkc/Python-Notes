# user_info={'name':'pratik hancy','age':23}
# print(user_info)
# print(type(user_info))
# # 2nd way
# user_info=dict(name="pratik hancy", age=23)
# print(user_info)
# print(type(user_info))

user_info={
    'name':'pratik hancy',
    'age':23,
    'qualification':'Bca',
    'player':["messi","cr7","ramos"]
}
(user_info.popitem())
user_info.pop('age')
print(user_info)
print(user_info.get('qualification'))





# print(user_info['name'])
# #input key and value in dictonary
# # user_info["favmusic"]=['pops','rock']
# print(user_info)
# #deleting value
# user_info["favmusic"].pop()
# print(user_info)

# #adding value in dictonary
# user_info['player'].append("ronaldo")
# print(user_info)

# for i in user_info.values():
#     print(i)

# for i,j in user_info.items():
#     print(f"this key is {i} and the value is {j}")


# print(user_info[player[0]])


# user_info.add('favmovie'='inception')
# print(user_info)

# #method 
# user_info={
#     'name':'pawan gaywali',
#     'sex':'Male',
#     'Address':'Shankanagar',
#     'age':23,
# }

# user_info2={
#     'name':'Sushant Thakuri',
#     'sex':'Male',
#     'Address':'kotihawa',
# }

# user_info.update(user_info2)
# print(user_info)
#  user_info["favmusic"]=['pops','rock']
# dictonary={ }
# def cube():
#     for i in range(1,6):
#        dictonary[i]=i**3 
#     return dictonary
# print(cube())

# name=input("enter name")
# dictonary={ }
# def counting(par):
#     for i in par:
#         dictonary[i]=par.count(i)
#     return dictonary
# print(counting(name))



