X, Y = map(int, input().split())
total = X + (10 * Y)
if total >= 100:
    print("Yes")
else:
    print("No")
