#class showing 3 class

class myclass(object):
    def set_value(self,value):
        try:
            val = int(value)
        except ValueError:
            return
        self.val = value
    def show_value(self):
        print(self.val)
    def increment_value(self,inc):
        self.val += inc

#create a instance

a = myclass()
a.set_value(10)
a.show_value()
a.increment_value(1)
a.val = 100
a.show_value()

#example shows the value of the variable can be changed through direct
#manipulation of the val
