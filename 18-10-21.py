list1 = ["hello","world","glad","to","be","alive"]
blaa = ["1","2","3"]

#copy list to another list

list2 = list1 #or
list3 = list1.copy()#or
list4 = list(list1)

print(list4)
print(list3)
print(list2)

#join list methods

foo = list1 + blaa
print(foo)  #or

for i in foo: 
    blaa.append(i)
print(blaa)

#or

list1.extend(blaa)
print(list1)

"""
append ()       Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	        Sorts the list

"""

