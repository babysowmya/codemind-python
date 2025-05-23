x = int(input())
for i in range(1, x + 1):
    y, a, b = map(int, input().split())
    print(((y + 1) // 2) * b + (y // 2) * a)
