import random


def reverse_string(s):
    s =" " + s
    return  s[11:0:-1]

mylist = ['hello','where','are','you']
str = "hello_world"
print(reverse_string(str))
#print(str[11:0:-1])
print(mylist)
print(mylist[1:3])
print(mylist[-1])
print(mylist[:3])
print(mylist[-3:0])

if "where" in mylist :
    print(random.randrange(1,5))
# change list of items

mylist[0] = "hey"
print(mylist)
# change list of items
mylist[1:4] = ["what", "are" , "you"]
print(mylist)

#insert new items into list

mylist.insert(0 , "brooo!")
print(mylist)

#append items

mylist.append("nigga")
print(mylist)

#to append another list

mylist2 = ["bro","hello", "rasom"]
mylist.append(mylist2)
print(mylist)
print(mylist[6])

#to adda tuple

mutuple = ("hello","nalle","rasom")
mylist.append(mutuple)
print(mylist)

#extend function adds all the elements of tuple as single elements to the list

mylist.extend(mutuple)
print(mylist)

#remove elements

mylist.remove("hello")
print(mylist)

#pop funtion when executed removes the last element

mylist.pop()
print(mylist)

#delete fucniton implementation

del mylist[0]
print(mylist)

"""del mylist
print(mylist)""" # error rises as the list is deleted

#clear list clear the list but that list is available

mylist.clear()

print("\n",mylist)


