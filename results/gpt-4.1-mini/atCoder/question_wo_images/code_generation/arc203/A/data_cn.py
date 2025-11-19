import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 最大完美紀錄獎人數為 M + N - 1
    print(M + N - 1)