x = int(input())
for i in range(x):
    a = int(input())
    l = list(map(int,input().split()))
    c = 0
    for i in l:
        if i>=1000:
            c = c+1 
    print(c)
