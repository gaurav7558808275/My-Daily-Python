# arrays in python

myarray =["gaurav","is","a","coder"]

# length of array can be done through len() function

print(len(myarray))

# looping of array

for i in myarray:
    if(i == "gaurav"):
        print(i)
# traversing

x = myarray[0]
print(x)
x = myarray[1]
print(x)
x = myarray[2]
print(x)
#x = myarray[10]  #index out of range eror
#print(x)

#adding an array elemnt
myarray.append("developer")
print(myarray)

#remove the element at specified position

myarray.insert(4,"and") # add elements to specified position
print(myarray)

#print the reverse of an array


print(myarray.reverse()) # dont know why none is given back


# to find the index

print(myarray.index("is"))
