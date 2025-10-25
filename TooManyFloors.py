import math
x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = (a-1)//10+1
    d = (b-1)//10+1
    print(abs(c-d))
