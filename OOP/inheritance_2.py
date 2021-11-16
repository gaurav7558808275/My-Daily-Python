class animal(object):
    def __init_(self,name):
        self.name = name
    def eat(self,food):
        self.food = food

class dog(animal):
    def fetch(self,thing):
        print("%s runs behind %s" %(self.name,thing))

class cat(animal):
    def eat(self,food):
        print("%s eats %s" %(self.name,food)


              
