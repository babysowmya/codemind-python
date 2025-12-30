x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = a*10
    d = a*12
    if b>=c and b<=d:
        print("YES")
    else:
        print("NO")
