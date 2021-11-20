#powers program

ppow = lambda x,p : x**p
print(ppow(2,2))

def pow_2(num):
    return ppow(num,2)
def pow_3(num):
    return ppow(num,3)

# same function can be used for multiple uses!

print(pow_2(2))
print(pow_3(2))
