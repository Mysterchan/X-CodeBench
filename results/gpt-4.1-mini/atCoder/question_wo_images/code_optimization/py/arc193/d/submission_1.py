import sys
input = sys.stdin.readline

def solve(N, A, B):
    A_pos = [i for i, ch in enumerate(A) if ch == '1']
    B_pos = [i for i, ch in enumerate(B) if ch == '1']

    # If number of pieces differ, impossible
    if len(A_pos) != len(B_pos):
        return -1

    # Sort positions to match pieces one-to-one
    A_pos.sort()
    B_pos.sort()

    # Minimum operations is max distance any piece must move
    max_dist = 0
    for a, b in zip(A_pos, B_pos):
        dist = abs(a - b)
        if dist > max_dist:
            max_dist = dist

    return max_dist

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()
    print(solve(N, A, B))