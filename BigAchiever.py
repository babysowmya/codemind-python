x = int(input())
for i in range(x):
    b = int(input())
    l = list(map(int,input().split()))
    for j in range(len(l)):
        a = l[:j]
        c = 0
        for k in a:
            if k<l[j]:
                c = c+1
        if c==len(a):
            print("1",end = " ")
        else:
            print("0",end = " ")
    print("\n")
