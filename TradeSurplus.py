a = int(input())
for i in range(a):
    a,b,c,d = map(int,input().split())
    e = a-b 
    f = c-d
    g = e+f
    if g<0:
        print("YES")
    else:
        print("NO")
