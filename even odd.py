def result(y):
    for i in y:
        if(i % 2 == 0):
            print("the", i , " is even")
        else:
            print("the", i , " is odd")



y = []
item1 = int(input("enter the value 1 :  "))
item2 = int(input("enter the value 2 : "))
y.append(item1)
y.append(item2)

result(y)
#print(y)
