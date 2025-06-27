arr = tuple(map(int, input().split()))
x = int(input())
c = 0
for i in range(0,len(arr)):
    if arr[i]==x:
        c = i
        f = 1
if f==1:
    print(c)
else:
    print("0")
