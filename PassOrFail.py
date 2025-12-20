x = int(input())
for i in range(x):
    a,b,c = map(int,input().split())
    d = b*3
    e = (a-b)
    if d-e>=c:
        print("PASS")
    else:
        print("FAIL")
