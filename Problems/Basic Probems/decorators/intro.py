#basic decorator function prototype

def print1(msg):
    print(msg)
def print2(func,msg):
    print1(msg)

print2(print1,"hey")