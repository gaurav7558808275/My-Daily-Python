 # classes in python and objects

#creating a class is as follows

class Me:
    y = 10
    print("you are in a class")

x = Me()  # to create an object
print(x.y)

# usage of a class with _init_()
# never forget to use double underscore
class classroom:
    def __init__(self,row,rolumn):
        self.row = row
        self.column = rolumn

    def func(blaa): # instead of using 
        print("The number of rows " + str(blaa.row))

d = classroom(10,20)
print(d.row)
print(d.column)
#having function inside a class
d.func()


#change the class value

d.row = 11
print(d.row)


#del command used to delete any element

del d.row

#del  the object also

del d
