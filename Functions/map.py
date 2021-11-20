#learning map function
#basic syntax will be map(fun,iter)
# fun can be basic function iter some iterable funtion
#it can be made returns as a  list/array or a set

nums= [1,2,3,4,5,6]

def sq(n):
    return n*n

list_1 = list(map(sq,nums))
print(list_1)

#returns[1, 4, 9, 16, 25, 36]
