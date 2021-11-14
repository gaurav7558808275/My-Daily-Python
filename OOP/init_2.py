
#here we pass the init() function with 
class num():
    def __init__(self,val):
        print("in init()")
        try:
            val = int(val)
        except ValueError :
            return
        self.val = val
    def increment(self):
        self.val+= 1
        print("the ncrement is " + str(self.val))

a = num(10)
a.increment()
