x = int(input())
for i in range(x):
    a,b,c,d = map(int,input().split())
    print(max(abs(a-c),abs(b-d)))
