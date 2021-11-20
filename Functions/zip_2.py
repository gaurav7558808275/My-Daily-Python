#zip function joins list and gives out a tuple
name = ["Manjeet", "Nikhil", "Shambhavi"]
roll_no = [4, 1, 3]
marks = [40, 50, 60]

zap = zip(name,marks)
#key-value pairs!
print(dict(zap))