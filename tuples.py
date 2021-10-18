#python tuples
#tuples allow duplicate values
#order must not be changed

tuple1 = ("gaurav","is","Pyhtonista","gaurav")
print(tuple1)
print(tuple1[0])
print(tuple1[::-1]) #reverse

#to add values to tuple we need convert first to a list

x = list(tuple1)
x.append("phadke")
tuple1 = tuple(x)
print(tuple1)

#add tuples

tuple2 = ("great","carrom")
x = list(tuple1) + list(tuple2)
tuple1 = x
print(tuple1)

#remove items

y = list(tuple1)
y.remove("carrom")
tuple1 = tuple(y)
print(tuple1)

#unpack of tuples (some feature )

veggies = ("carrot","tomato","beans","ballal")
(orange,red,*green) = veggies

print(orange)
print(green)
print(red)

#looping through tuple

for i in tuple1:
    print(i,end = "\n")
    
#tuple count() function
print(tuple1.count("gaurav"))
print(tuple1.index("gaurav"))


