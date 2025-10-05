n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    c = a*b 
    print(c//60,end = " ")
    print(c%60,end = "\n")
