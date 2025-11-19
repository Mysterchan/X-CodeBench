import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = min(n, m) - 1
    # Maximum perfect record players = 2^(min(n,m)-1)
    # Use left shift for fast power of two calculation
    print(1 << a)