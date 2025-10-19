x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = a-(0.1*a)
    if c<b:
        print("ONLINE")
    elif c>b:
        print("DINING")
    else:
        print("EITHER")
