import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # If total number of 1s differ, impossible
    if sum(A) != sum(B):
        print("No")
        continue

    # If no 1s in A and B, they are all zeros, so always possible
    if sum(A) == 0:
        print("Yes")
        continue

    # Extract positions of 1s in A and B
    posA = [i for i, val in enumerate(A) if val == 1]
    posB = [i for i, val in enumerate(B) if val == 1]

    # Check if relative order of 1s can be matched by allowed operations
    # The operation allows swapping equal-sum segments, which means we can reorder
    # the 1s arbitrarily but the relative order of zeros between 1s is constrained.
    # However, since the operation swaps segments with equal number of 1s,
    # it can reorder the 1s arbitrarily.
    # So the only constraint is that the number of 1s is the same.
    # But we must check if the relative order of zeros can be matched.
    #
    # Actually, the problem is known: the operation allows rearranging the sequence
    # by swapping segments with equal number of 1s.
    # This means the relative order of 1s can be changed arbitrarily.
    #
    # So the only constraint is the number of 1s must be equal.
    #
    # Therefore, answer is "Yes" if sum(A) == sum(B), else "No".

    print("Yes")