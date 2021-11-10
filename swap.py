
def swap(data):
    length = len(data)
    t = data[0]
    data[0] = data[length -1]
    data[length -1] = t

    return data
    




data = [10,11,12,13,14]
r = swap(data)
print(r)
