x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    y = b-a
    z = c-b
    if y==z:
        print("0")
    else:
        print("1")