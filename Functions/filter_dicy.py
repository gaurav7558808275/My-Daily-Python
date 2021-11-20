#handling dictionaries

users = [
    {"username": 'samuel', "tweets": ["i love cake", "i am good"]},
    {"username": 'andy', "tweets": []},
    {"username": 'kumal', "tweets": ["India", "Python"]},
    {"username": 'sam', "tweets": []},
    {"username": 'lokesh', "tweets": ["i am good"]},
]

list_1 = filter(lambda x : x["tweets"] , users)
#print(list(list_1))

list_1 = filter(lambda x : not x["tweets"] , users)
#print(list(list_1))

list_2 = filter(lambda x : x["username"].upper(),users)
#print(list(list_2))

names = list(map(lambda x : x["username"] , filter(lambda x : len(x["username"]) > 4,users)))
#printing names greater than 4 letters
print(list(names))