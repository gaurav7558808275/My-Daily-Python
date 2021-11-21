#learning the try: and except programs

import os
randomlist = ['a',0,2]
for data in randomlist:
    try:
        print("first entry is " + data)
        r = 1/int(data)
        break
    except Exception as ex:
        print("this " , str(ex.__class__),"occured")
        print()
print("the reciprocal of" , data, "is ", r)

