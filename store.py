x = int(input())
for i in range(1,x+1):
    a,b = map(int,input().split())
    if a<b:
        c = b-a
        print(a+(c*2))
    else:
        print(b)
