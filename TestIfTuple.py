arr = tuple(map(int, input().split()))
c = []
a = 0
for i in arr:
    if i not in c:
        c.append(i)
    else:
        a = a+1
if a>0:
    print("False")
else:
    print("True")
