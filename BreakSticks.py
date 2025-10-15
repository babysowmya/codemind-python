x = int(input())
for i in range(x):
    a = int(input())
    l = list(map(int,input().split()))
    print(sum(l)-len(l))
