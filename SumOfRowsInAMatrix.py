a,b = map(int,input().split())
r = []
for i in range(a):
    l = list(map(int,input().split()))
    r.append(l) 
for i in range(a):
    m = list(map(int,input().split()))
    for j in range(b):
        r[i][j]+= m[j]
for i in range(a):
    for j in range(b):
        print(r[i][j],end = " ")
    print()
