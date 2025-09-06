t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a>=b:
        print(b)
    else:
        c = a+(b-a)*2
        print(c)
