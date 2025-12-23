x = int(input())
for i in range(x):
    a,b,c,d = map(int,input().split())
    r = a-(b+c)
    if r>=d:
        print("0")
    elif r+max(b,c)>=d:
        print("1")
    else:
        print("2")
