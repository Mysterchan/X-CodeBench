import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# We want to find the maximum K such that we can form K pairs (a,b)
# with a <= b/2, using 2K mochi from the sorted list A.

# Approach:
# Use binary search on K.
# For a given K, check if it's possible to pair the smallest K mochi
# with the largest K mochi satisfying the condition.
# Since A is sorted, we try to pair A[i] with A[N-K+i].
# If for all i in [0, K-1], A[i] <= A[N-K+i] / 2, then K is possible.

def can_make(k):
    for i in range(k):
        if A[i] * 2 > A[N - k + i]:
            return False
    return True

left, right = 0, N // 2
while left < right:
    mid = (left + right + 1) // 2
    if can_make(mid):
        left = mid
    else:
        right = mid - 1

print(left)