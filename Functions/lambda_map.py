#using lmabda function in map function
num = [1,2,3,4,5,6]
x_1=lambda x,y  : x**y
#creating the triple function from the lambda function.
def triple(num):
    return x_1(num,3)
lis_1 = list(map(triple, num))
print(lis_1)
