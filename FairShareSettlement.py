import math
x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = math.floor(a/(b+1))
    print(a-(b*c))
