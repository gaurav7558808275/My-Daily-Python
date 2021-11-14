#creating a container class

class mainclass(object):
    def set_value(self,val):
        self.value = val
    def ge_value(self):
        return self.value

#initialisation of a class instance

a = mainclass()
b = mainclass()

a.set_value(10)
b.set_value(100)

print (a.ge_value())
print(b.ge_value())        
        
