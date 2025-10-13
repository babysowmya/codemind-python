T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    total = 3 * min(A, B // 2)
    print(total)
