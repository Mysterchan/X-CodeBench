import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A.sort()
if n % 2 == 0:
    # For even n, max sum of absolute differences by pairing smallest half with largest half
    half = n // 2
    ans = sum(A[half:]) - sum(A[:half])
else:
    # For odd n, try removing each element at even indices and compute max
    half = (n - 1) // 2
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]

    ans = 0
    # Precompute sums for left and right parts to avoid repeated sum calls
    # For each i in even positions, remove A[i], then sum of right half - sum of left half
    for i in range(0, n, 2):
        left_sum = prefix[i]  # sum of elements before i
        right_sum = prefix[n] - prefix[i + 1]  # sum of elements after i
        # Number of elements in left and right parts after removal
        left_len = i
        right_len = n - i - 1
        # half length for left and right parts
        left_half = left_len // 2
        right_half = right_len // 2

        # sum of largest half in left part
        left_largest = prefix[i] - prefix[i - left_half] if left_half > 0 else 0
        # sum of smallest half in left part
        left_smallest = prefix[left_half] if left_half > 0 else 0

        # sum of largest half in right part
        right_largest = prefix[n] - prefix[n - right_half] if right_half > 0 else 0
        # sum of smallest half in right part
        right_smallest = prefix[i + 1 + right_half] - prefix[i + 1] if right_half > 0 else 0

        # Actually, the solve function is sum of largest half - sum of smallest half
        # So for left part:
        left_score = (prefix[i] - prefix[i - left_half]) - prefix[left_half] if left_half > 0 else 0
        # For right part:
        right_score = (prefix[n] - prefix[n - right_half]) - (prefix[i + 1 + right_half] - prefix[i + 1]) if right_half > 0 else 0

        total = left_score + right_score
        if total > ans:
            ans = total

print(ans)