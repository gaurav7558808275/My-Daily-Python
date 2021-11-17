# polymorphism are methods having same name put different behaviour/ functionalities

class car:

    def description(self):
        print("this is car calss with same name")

class bus:
    def description(self):
        print("this is calss bus with same name")

#create an object of class car and bus
a= car()
b = bus()

a.description()
b.description()

#prints without error
