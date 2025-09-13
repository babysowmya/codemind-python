t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    res = (5*a)+(b*10)
    print(res//c)
