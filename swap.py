
def swap(data):
    length = len(data)
    t = data[0]
    data[0] = data[length -1]
    data[length -1] = t

    return data

def swap2(data):
    data[0],data[-1] = data[-1],data[0]
    return data

def swap3(data):
    r = data[0],data[-1]
    data[-1],data[0] = r
    return data
def swap4(data4):
    a,*b,c = data4
    data4 = [c,*b,a]
    return data4
def swap4(data5):
    first = data.pop(0)
    last - data.pop(-1)

    data.insert(0,last)
    data.append(first)
    return data5
    


data1 = [10,11,12,13,14]
data2 = [10,11,12,13,14]
data3 = [10,11,12,13,14]
data4 = [10,11,12,13,14]
data5 = [10,11,12,13,14]
r = swap(data1)
print(swap2(data2))
print(swap3(data3))
print(r)
print (swap2(data4))
print (swap2(data5))
