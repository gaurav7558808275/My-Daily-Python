#reduce function learning
#to ind the sum of all the numbers
from functools import reduce
s = [1,2,3,4,5,6]
sum = reduce(lambda a,b : a+b , s)
print(sum)
mul = reduce(lambda a,b  : a*b, s)
print(mul)