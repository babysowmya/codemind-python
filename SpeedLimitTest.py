x = int(input())
for i in range(x):
    a,b,c,d = map(int,input().split())
    if (a/b)<(c/d):
        print("Bob")
    elif (a/b)>(c/d):
        print("Alice")
    else:
        print("Equal")
