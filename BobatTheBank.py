x = int(input())
for i in range(x):
    a,b,c,d = map(int,input().split())
    if b>c:
        print(a+(b-c)*d)
    else:
        print(a-(c-b)*d)
