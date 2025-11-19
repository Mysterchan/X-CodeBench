import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    total_A = 0
    total_B = 0
    total_C = 0
    for __ in range(N):
        A, B, C = map(int, input().split())
        total_A += A
        total_B += B
        total_C += C

    # Each C2C requires:
    # Div.1: 1 hard (A) + 1 medium (B)
    # Div.2: 1 medium (B) + 1 easy (C)
    #
    # Each medium problem can be used at most once in either Div.1 or Div.2 per C2C.
    #
    # Let x = number of C2C contests
    # We need:
    #   A >= x (hard problems for Div.1)
    #   C >= x (easy problems for Div.2)
    #   B >= 2x (medium problems total, since each C2C uses 2 medium problems: one in Div.1 and one in Div.2)
    #
    # So maximum x = min(total_A, total_C, total_B // 2)

    ans = min(total_A, total_C, total_B // 2)
    print(ans)