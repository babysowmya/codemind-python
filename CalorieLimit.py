x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    l = list(map(int,input().split()))
    c = 0
    d = 0
    for j in l:
        c = c+j
        if c<=b:
            d = d+1
    print(d)
