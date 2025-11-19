import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    xor_sum = 0
    for _ in range(k):
        x, y = map(int, input().split())
        xor_sum ^= (y - 1)
    print("Mimo" if xor_sum else "Yuyu")
