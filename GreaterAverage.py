x = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    aver = (a+b)/2
    if(aver>c):
        print("YES")
    else:
        print("NO")
