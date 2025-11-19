import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sumA = sum(A)
    sumB = sum(B)
    if sumA != sumB:
        print("No")
        continue

    # If sumA == 0, all zeros, no swaps needed
    if sumA == 0:
        print("Yes" if A == B else "No")
        continue

    # Extract positions of 1s in A and B
    posA = [i for i, v in enumerate(A) if v == 1]
    posB = [i for i, v in enumerate(B) if v == 1]

    # The operation allows swapping equal-sum segments.
    # Since sumA == sumB, number of ones is same.
    # We can reorder the ones arbitrarily by swapping segments with equal number of ones.
    # So the only constraint is that the relative order of zeros and ones can be changed arbitrarily.
    # But zeros cannot be moved across ones without matching sums.
    # Actually, the operation allows swapping any two segments with equal number of ones.
    # This means we can reorder the ones arbitrarily.
    # So the only constraint is that the number of ones is the same.
    # Therefore, answer is always "Yes" if sumA == sumB.

    # But the problem states the operation swaps segments with equal sum.
    # Since sum is number of ones, swapping segments with equal number of ones.
    # This allows arbitrary permutation of the ones.
    # So any sequence with same number of ones can be transformed into any other sequence with same number of ones.

    # So answer is "Yes"
    print("Yes")