import datetime


x= datetime.datetime.now()
print(x.year)
print(x.day)

#strfname is used for formatting use %
# a and A fro days
# b and B for months
# w weekday number from 1-7
# d day of the month from 1-30
# m as month numers 1-12
# G ISO year 

print(x.strftime("%f"))

#abs() real and imaginary is present it retrun the real part
print(abs(22.22))
#aiter()

#all() retrun truw if all the iterables return true.

list = [1,2,3,4,5]
print(str(all(list)))
# ascii of the object
str = "gaurav + is"
print(ascii(str))

# bin() starts with 0b to indcate starts with binary
print(bin(2))
print(bin(-2))

#bool() if false it returns false otherwise true.

#bytrearray(source,encoding,error) syntax
str = "gaurav is great"
print(str.encode())
str1 = bytearray(str,'utf-8')
str2 = bytearray(str,'utf-16')
print(str1)
print(str2)
