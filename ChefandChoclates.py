import math
x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    d = (a*5)+(b*10)
    e = abs(d/c)
    print(math.floor(d/c))
