#usage of Inheritance in classes

#parent class  inherited from also knows as base class
#child class or derived class

class man:
    def __init__(self,Name,Rollno):
        self.name = Name
        self.rollno = Rollno
    def add(self):
        print(self.name ,self.rollno,)

# create inheritance or child process

class man1(man):
    #pass
    def __init__(self,Name,Rollno):
        man.__init__(self,Name,Rollno)
        

x = man1("gaurav" , 20)
x.add()

#There is a Super function that will automatically inherit the parent features

class man2(man):
    def __init__(self,Name,Rollno,year):
        super().__init__(Name,Rollno)
        self.graduationyear = year
    def print(self):
        print(self.name , self.graduationyear , self.rollno)

#adding another parameter in this class.

y = man2("Kumar" , 10 , 2019)
y.add()
y.print()
