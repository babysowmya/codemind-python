import math
def posAverage(numbers,size):
    c = []
    for i in numbers:
        if i>=0:
            c.append(i)
    return math.floor(sum(c)/len(c))
