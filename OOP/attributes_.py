# difference between class attribute and instance attribute

class blaa():
    value = 10
    print(str(value))
    def change(self):
        value = 20
        print(str(value))
class new():
    classy = 10
    print(str(classy))



#nitiated the attribute value
a = blaa()
a.change() # initiated the instance

b= new()
b.classy
b.classy2 = 10
print(str(b.classy2))
del b.classy2  # this will delete the instance
