def largest(arr):
    max = arr[0]
    for i in arr:
        if(arr[i] > max):
            max = arr[i]
    return max

array1 = [3,5,7,6,5,7,8,4,6]
print(largest(array1))