T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(M * (N - 1))