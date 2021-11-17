class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def description(self):
         print(f"{self.name} is aged {self.age}")
    def __str__(self):
        return f"{self.name} is aged {self.age}" #implementation of dunder files.
a = dog("fluffy",10)
b = dog("chuffu",20)
a.description()
b.description()

print(a)
print(isinstance(a,dog)) #isinstance functon to check whether it is available or not.
