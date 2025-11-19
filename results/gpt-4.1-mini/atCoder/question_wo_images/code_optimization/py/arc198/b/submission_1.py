import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    # Based on problem analysis and sample tests:
    # The sequence exists if and only if:
    # 1) x >= z (to avoid negative n00)
    # 2) y <= 2*z (to satisfy n02 >= y)
    if x >= z and y <= 2 * z:
        print("Yes")
    else:
        print("No")