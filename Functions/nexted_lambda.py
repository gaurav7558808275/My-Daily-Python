#finding the largest usig lambda function

largest = lambda a,b,c,d : a if a>b and a>c and a>d else (b if b>a and b>c else(c if c>a and c>b and c >d else(d)))

print(largest(1,2,3,4))