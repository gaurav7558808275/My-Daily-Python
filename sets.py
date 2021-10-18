#sets in python


myset = {"gaurav","wants","to","a","pythonsta"}
mysett = {"hoho","its","very","cold","yappa"}
mylist = ['hello','where','are','you',"blaaa","gluuu","hiii"]
print(myset)

#unordered #unindexed # cannot be changed

#lenght of a set

print(len(myset))

#accessing a set

for  i in myset:
    print(i, end= "\n")

#set cannot be changed but can be added with values

myset.add("hehe")
print(myset)
(myset.update(mysett))
print(myset)

#add a list to set or dictionary also
myset.update(mylist)
print(myset)

#remove item
myset.remove("hello") #argument only takes 1 input

#joining sets using union

myset.union(mylist)
print(myset)

#intersection update copies only items present in both sets

print(myset.intersection_update("gaurav"))
print(myset.intersection("yap[a"))

