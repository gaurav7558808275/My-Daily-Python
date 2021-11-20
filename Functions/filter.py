#Learning filter function 
#syntax is filter[fun,iter]

num = [1,2,3,4,5,6]
list_1 = filter(lambda x:x%2!=0,num)
print(list(list_1))
list_2 = filter(lambda y : y %2 ==0,num)
print(list(list_2))