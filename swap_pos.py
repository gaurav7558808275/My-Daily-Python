def swap1(data1):
    data1[pos1],data1[pos2] = data1[pos2],data1[pos1]
    return data1
def swap2(data2):
    temp  = data2[pos1]
    data2[pos1] = data2[pos2]
    data2[pos2] = temp
    return data2
def swap3(data3):
    *a,b,c,d = data3
    data3 = [*a,c,b,d]
    return data3
def swap4(data4,pos1,pos2):
    s1 = data4.pop(pos1)
    s2 = data4.pop(pos2-1)
# PROBLEMS OF THE POP OPERATOR PERSISTS
    data4.insert(pos1,s2)
    data4.insert(pos2,s1)
    
    return data4


data1 = [1,2,3,4,5,6]
data2 = [1,2,3,4,5,6]
data3 = [1,2,3,4,5,6]
data4 = [1,2,3,4,5,6]
pos1 = 3
pos2 = 4
print(swap1(data1))
print(swap2(data2))
print(swap3(data3))
print(swap4(data4,pos1,pos2))
