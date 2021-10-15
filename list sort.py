# lits loops

mylist = ["hello","bro","nice","to","meet","you","crazy shit"]

#loopingthrough items

for i in mylist:
    print(i)
# loop through index number
print("\n")
for i in range(len(mylist)):
    print(mylist[i])

#using a while loops
print("\n")
i=0
while(i < len(mylist)):
    print(mylist[i])
    i+=1

#list comprehension
print("\n")
[print(i) for i in mylist]

#lits comprehension continued
#one line for elements having an 'b'

newlist = [i for i in mylist if "b" in i]
print(newlist)

#practice short hand

print("\n")
str = " hello_ world"
rev = [print(i) for i in str if i !=" "]

#list sorting

mylist.sort()
print(mylist)

#ascendin
mylist.sort(key = None , reverse = True)
print(mylist)

# just an idea, we could develop a sorting algorithm when entered a jumbled set
# words we recieve a readable sentence.

#customised sort function # not working currently as no logic

def sort(str):
    return str.upper()

mylist.sort(key = sort)
print(mylist)

