x = int(input())
for i in range(x):
    a,b,c,d = map(int,input().split())
    if (a+b+c)<d or (a+b+d)<c or (a+c+d)<b or (b+c+d)<a:
        print("YES")
    else:
        print("NO")
