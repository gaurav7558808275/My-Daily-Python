#Playing around the datetimelibrary and math library

import math
import datetime
import json

x = datetime.datetime.now()
print(x)
print(x.year)  # year 
print(x.strftime("%A ")) # Prints day takes a format speifier
print(x.strftime("%B"))  # this returns the month


#playing around the math function

x = min(5,10,40)
y = max(1,2,3)
print(x,y)

# absolute value of the number

z = abs(-54)
print(z)

print(math.sqrt(56))


x = {
    "name"  : "gaurav",
    "age"   :    "25",
    "place" : "bangalore",
    "interests" : "embedded developer"
        }
print(json.dumps(x,indent = 4, separators = (", ", ": ")))

