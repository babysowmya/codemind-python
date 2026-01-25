from collections import Counter
x = int(input())
for i in range(x):
    a = int(input())
    l = list(map(int,input().split()))
    res = []
    c = Counter(l)
    m = max(c.values())
    for i in c:
        if c[i]==m:
            res.append(i)
    print(min(res))
