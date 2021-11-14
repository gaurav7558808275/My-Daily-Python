#the init constructor is a magic method which gets called when a
# class is instanciated

#create a class

class myclass(object):
    def set_value(z,val):
        z.value = val
    def show_value(z):
        print(z.value)


a = myclass()
a.set_value(10)
a.show_value()

# example to show we can change the value without using the
#functions initiated in class
a.value = 100
a.show_value()
