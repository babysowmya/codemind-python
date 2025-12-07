x = int(input())
for i in range(x):
    a,b,c = map(int,input().split())
    if a<=3:
        print(a*b)
    else:
        d = a//3
        e = a%3
        if e==0:
            d = d-1
        print((a*b)+(c*d))
