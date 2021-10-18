#python dictionary
#key : value pairs
#as of python 3.7 ordered
#no duplicates, changeable


mydict = {"date":  '14',
          "month" : 'january',
          "year"  :  '1996'}

print(mydict)

print(mydict["month"])
print(len(mydict)) #length
print(type(mydict))

#accessing dictionary
print(mydict.get("date"))

print(mydict.keys())
print(mydict.values())

#adding a new member with key and values

mydict["era"] = "someshit"
print(mydict)




