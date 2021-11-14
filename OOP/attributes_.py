# difference between class attribute and instance attribute

class blaa():
    value = 10
    print(str(value))
    def change(self):
        value = 20
        print(str(value))

#nitiated the attribute value
a = blaa()
a.change() # initiated the instance

