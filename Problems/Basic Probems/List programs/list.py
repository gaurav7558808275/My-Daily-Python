#list program to repalce the contents of the list

mylist = [1,2,3,4,5,6]
print(mylist)
mylist[0],mylist[-1] = mylist[-1],mylist[0]
print(mylist)