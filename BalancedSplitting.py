x = input()
l = 0
r = 0
c = 0
for i in x:
    if i=="L":
        l = l+1
    else:
        r = r+1
    if l==r:
        c = c+1
print(c)
