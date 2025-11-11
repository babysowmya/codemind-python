x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    if ((a+b)//2)%2==0:
        print("Alice")
    else:
        print("Bob")
