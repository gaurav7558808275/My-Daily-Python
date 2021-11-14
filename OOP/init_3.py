

class main(object):
    count =0
    print("initiated")
    def __init__(self,val):
        self.val = val
        main.count +=1
        
    def set_value(self,val):
        self.val = val
        
    def get_value(self):
        print(str(self.val))
        
    def get_count(self):
        print(str(main.count))

a = main(2)
b = main(2)
for o in (a,b):
    print(o.get_value())
    print(o.get_count())

