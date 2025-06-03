x = int(input())
for i in range(1,x+1):
    num =list(map(int,input().split()))
    num.sort()
    print(num[1])
    
