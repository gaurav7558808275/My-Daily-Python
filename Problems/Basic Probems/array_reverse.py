#reverse array using slicing method

array1 = [1,2,3,4,5,6]
d = len(array1)
n = input("Enter the position")
temp = array1[0:int(n)]
print(temp)
new_array= array1[int(n):d]
temp = temp + new_array
print(temp)
