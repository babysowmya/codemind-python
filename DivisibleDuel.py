x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = []
    d = []
    for i in range(a,b+1):
        if i%a==0:
            if i%2==0:
                c.append(i)
            else:
                d.append(i)
    if sum(c)>=sum(d):
        print("YES")
    else:
        print("NO")
