x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = (500-(a*2))+(1000-(a+b)*4)
    d = (1000-(b*4))+(500-(a+b)*2)
    if c>d:
        print(c)
    else:
        print(d)
