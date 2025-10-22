x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c =21-(a+b)
    i=1
    if c<=10:
        print(c)
    else:
        print("-1")
