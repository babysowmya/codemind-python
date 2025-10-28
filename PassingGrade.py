x = int(input())
for i in range(x):
    a = int(input())
    lst = list(map(int,input().split()))
    c = 0
    for i in range(len(lst)):
        if lst[0]<=lst[i]:
            c = c+1
    print(c)
