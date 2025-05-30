T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd_days_total = sum(A[i] for i in range(0, N, 2))
    even_days_total = sum(A[i] for i in range(1, N, 2))
    print(max(odd_days_total, even_days_tot
