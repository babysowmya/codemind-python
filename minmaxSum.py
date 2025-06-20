lst = list(map(int,input().split()))
a = max(lst)
b = min(lst)
min = sum(lst)-a
max = sum(lst)-b
print(min,max)
