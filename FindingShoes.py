x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if a<b:
        print(a)
    else:
        print(2*a-b)
