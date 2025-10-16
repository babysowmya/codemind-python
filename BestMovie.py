x = int(input())
for i in range(x):
    a = int(input())
    c = []
    for i in range(a):
        x,y = map(int,input().split())
        if x>=7:
            c.append(y)
    if not c:
        print("-1")
    else:
        print(min(c))
