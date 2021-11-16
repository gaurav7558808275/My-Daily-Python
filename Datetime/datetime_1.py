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
