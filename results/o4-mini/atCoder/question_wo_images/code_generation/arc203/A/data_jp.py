import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 最大値は (N-1)*M
    print((N - 1) * M)