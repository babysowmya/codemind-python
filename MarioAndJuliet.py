x = int(input())
for i in range(x):
    a,b,c = map(int,input().split())
    d = b//a 
    if d>c:
        print("0")
    else:
        print(c-d)
