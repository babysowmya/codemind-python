x = int(input())
for i in range(x):
    a,b,c = map(int,input().split())
    z = [a,b,c]
    x = max(z)
    z.remove(x)
    print(max(z))
