x = int(input())
for i in range(x):
    a = int(input())
    c = 0
    if a%5!=0 and a%10!=0:
        print("-1")
    else:
        t = a//10
        r = a%10
        f = r//5
        print(t+f)
