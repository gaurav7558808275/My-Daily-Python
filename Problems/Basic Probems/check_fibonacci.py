#problem to check if the number is perfect sqaure
import math

def perfect_square(num):
    s = int(math.sqrt(num))
    return (s*s == num)
    #this will return true
def fibo_check(x):
    return perfect_square((5*(x*x)+4)) or perfect_square((5*(x*x)-4))

for i in range(1,11):
    if(fibo_check((i)) == True):
        print(str(i) + " Is a fibo")
    else:
        print(str(i) + " Not a Fibo")