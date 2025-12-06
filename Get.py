r = int(input())
for i in range(r):
    a,b,c = map(int,input().split())
    d = min(a,b,c)
    e = d*10
    x = a-d
    y = b-d
    z = c-d
    res = (x*3)+(y*3)+(z*3)
    print(e+res)
