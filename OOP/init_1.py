#__init__() constructor explanation
#__init__() sets the initial value or setup when c cclass instnatiated.


class myclass():
    def __init__(self):
        print("__init__() is executed")
        self.val = 0
    def set_value(self,val):
        self.val = val
        print("self.val ="+ str(self.val) + " this value is initiated")

a= myclass()
a.set_value(100)

#example for constructor __init__() function
