t = int(input())

for _ in range(t):
    X, Y = map(int, input().split())
    new_profit = Y + (X // 10)
    print(new_profit)
