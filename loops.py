#loops
#short hand

a=10
b=11

print("ä is greater")if a>b else print("b is greater") #for 2 condition short hand
#for 3  
print("ä is greater")if a>b else print("=") if a==b else print("b is greater")

#pass functions

if(a==b):
    pass
    print("pass worked")

#continue in for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

