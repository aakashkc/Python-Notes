# user_info={'name':'pratik hancy','age':23}
# print(user_info)
# print(type(user_info))
# # 2nd way
# user_info=dict(name="pratik hancy", age=23)
# print(user_info)
# print(type(user_info))

# user_info={
#     'name':'pratik hancy',
#     'age':23,
#     'qualification':'Bca',
#     'player':["messi","cr7","ramos"]
# }
# (user_info.popitem())
# user_info.pop('age')
# print(user_info)
# print(user_info.get('qualification'))


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

# creating a dictonary

# fastest way to create a dictonary is by using {}
dictonary1 = {"name": "Aakash", "age": 23, "qualification": "Bca"}
dictonary2 = dict(name="KC", age=28, qualification="Bcas")
# Accessing values in dictonary
# print(dictonary1["name"], "key error if key is not found")
# print(dictonary2.get("name"), "None if key is not found")
# print(dictonary2.get("name", "AK"), "default value if key is not found")
#  get method is better than [] because it does not give error if key is not found

# adding/updating values in dictonary
# dictonary2["name"] = ["Akash KC"]
# dictonary2.update(
#     {"name": "Akash Chhetri", "passion": "coading"}
# )  # merge multiple value at once in dictonary
# print(dictonary2)

# Removing value in dictonary
# del dictonary2["age"]  # error if key is not found
# dictonary2.pop(
#     "name"
# )  # remove and return the value of the key, error if key is not found
# dictonary2.pop(
#     "name", "None"
# )  # remove and return the value of the key,None if key is not found
# print(
#     dictonary2.popitem()
# )  # remove and return the last key-value pair as a tuple, error if dictonary is empty
# print(dictonary2)


# Looping in dictonary
# for key, value in dictonary1.items():
#     print(key, value)

# for value in dictonary1.values():
#     print(value)

# diccopy = (
#     dictonary1.copy()
# )  # create a shallow copy of the dictonary without modifying the original dictonary
# print(diccopy, "this is copy of dictonary1")

# setdefault() in dictonary useful in counting / grouping dictonary
# it is helpful in counting the frequency of the elements in a list or string and grouping the elements in a dictonary
# avoids checking if the key is already present in the dictonary
# setdefault(key,default_value) returns the value of the key if it is present in the dictonary, otherwise it inserts the key with the default value and returns the default value
# print(dictonary1.setdefault("namee", "default value"))
# print(dictonary1, "after default value set")

# withoutsetdefault()
# num = [1, 1, 1, 2, 2, 3, 3, 4, 5]
# expout = {}
# for i in num:
#     if i not in expout:
#         expout[i] = 1
#     expout[i] = expout[i] + 1
# print(expout, " this is expected output without setdefault()")

# num = [1, 1, 1, 2, 2, 3, 3, 4, 5]
# expout = {}
# for key in num:
#     expout.setdefault(key, 0)
#     expout[key] += 1

# print(expout, " this is expected output with setdefault()")

# dic = {"name": ["hello", "hi", "hey"], "age": [23, 24, 25]}
# print(
#     dic["name"].append("cyrax"),
#     "here we are accessing the value of the key 'name' which is a list",
# )
# print(dic)
# check if key is present in dictonary or not
words = ["apple", "ant", "bat", "ball", "cat", "car"]
# expout = {}
# for word in words:
#     if word[0] not in expout:
#         expout[word[0]] = []
#     expout[word[0]].append(word)
# print(expout, " this is expected output without setdefault()")
# with setdefault()
expout = {}
for word in words:
    expout.setdefault(word[0], []).append(word)
print(expout, " this is expected output with setdefault()")
