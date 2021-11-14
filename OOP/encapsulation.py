#creating a container class

class mainclass(object):
    def set_value(self,val):
        self.value = val
    def ge_value(self):
        return self.value

#initialisation of a class instance

a = mainclass()


a.set_value(10)


print (a.ge_value())
        
        
