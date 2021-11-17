#define a class
#we are able to use or access the calss variable through a mandled variable.

class car:
    def __init__(self,name,mileage):
        self.name = name
        self.__mileage = mileage
    def display(self):
        return f"the car is {self.name} and has mileage {self.__mileage}"
a = car("swift",15)
print(a.display()) # here the private function works in through the methods

#print(a.__mileage) # this wont allow direct access
print(a._car__mileage) 

# to allow direct access we will use the mangling method 
# syntax for name mangling will be {obj._classname__attribute}

