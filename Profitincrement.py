x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = a-b
    d = (a//100)*10
    print((a+d)-c)
