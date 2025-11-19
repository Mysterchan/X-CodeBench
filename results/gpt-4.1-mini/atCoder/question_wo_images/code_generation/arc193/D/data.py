import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()

    # Extract positions of pieces in A and B
    posA = [i for i, ch in enumerate(A) if ch == '1']
    posB = [i for i, ch in enumerate(B) if ch == '1']

    # If number of pieces differ, impossible
    if len(posA) != len(posB):
        print(-1)
        continue

    # Calculate the minimal number of operations needed
    # The minimal number of operations is the maximum absolute difference
    # between the positions of pieces in A and B when matched in order.
    max_diff = 0
    for a, b in zip(posA, posB):
        diff = abs(a - b)
        if diff > max_diff:
            max_diff = diff

    print(max_diff)