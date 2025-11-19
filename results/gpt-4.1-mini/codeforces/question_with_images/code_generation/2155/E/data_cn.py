import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grundy = 0
    for __ in range(k):
        x, y = map(int, input().split())
        # 根據題意，該遊戲的Nim值為 y-1
        grundy ^= (y - 1)
    print("Mimo" if grundy != 0 else "Yuyu")