x  = int(input())
for i in range(1,x+1):
    a,b,c = map(int,input().split())
    if a!=b and a!=c and b!=c:
        print("YES")
    else:
        print("NO")
