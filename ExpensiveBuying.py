x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    a = sorted(c,reverse=True)
    c = 0
    for i in range(b):
        c = c+a[i]
    print(c)
