import sys
input = sys.stdin.readline

MOD = 998244353

# Explanation:
# The problem asks for the sum of f(b) over all subarrays b of a.
# f(b) is the minimum number of operations to achieve the darkness pattern b.
#
# Key insight (from editorial and problem analysis):
# f(b) = number of distinct values in b minus 1.
# This is because each operation can add one "layer" of darkness to some folded stack,
# and folding allows overlapping cells with the same darkness to be combined.
#
# So for each subarray b, f(b) = (count of distinct elements in b) - 1.
#
# We need sum over all subarrays of (distinct_count - 1) = sum of distinct_count over all subarrays - total_subarrays
#
# total_subarrays = n*(n+1)//2
#
# So the problem reduces to:
# sum over all subarrays of distinct_count
#
# This is a classic problem: sum of number of distinct elements in all subarrays.
#
# We can solve it using a two-pointer approach:
# - Maintain a sliding window [l, r]
# - Keep track of frequency of elements in the window
# - For each r, move l as needed to maintain the window
# - For each r, the number of subarrays ending at r is (r - l + 1)
# - The number of distinct elements in the current window is len(freq)
# - We accumulate the sum of distinct elements over all subarrays by adding distinct_count for each subarray ending at r
#
# But we want sum of distinct elements over all subarrays, so we do:
# For each r, sum += distinct_count * (r - l + 1)
#
# However, this counts distinct elements for all subarrays ending at r.
# But we want sum over all subarrays, so we can do:
# For each r, we add distinct_count for all subarrays ending at r.
#
# Implementation detail:
# We'll use a two-pointer approach:
# - l = 0
# - For r in [0..n-1]:
#   - Add a[r] to freq
#   - While freq[a[r]] > 1 (or no need to shrink since duplicates allowed)
#   - Actually, we don't need to shrink window, we want all subarrays.
#
# Wait, we need sum of distinct elements over all subarrays.
#
# The standard approach is:
# For each position, count how many subarrays include that element as distinct.
#
# Another approach:
# Use the formula:
# sum of distinct elements over all subarrays = sum over all elements of (number of subarrays where element is present)
#
# For each element, find all its occurrences.
# For each occurrence at position i, the number of subarrays including this occurrence is:
# (i - prev_occurrence) * (next_occurrence - i)
#
# Sum over all occurrences and all elements.
#
# Then sum of distinct elements over all subarrays = sum over all elements and their occurrences of (i - prev) * (next - i)
#
# Then sum f(b) = sum_distinct - total_subarrays
#
# We'll implement this approach.

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Map each value to list of positions (1-based for convenience)
        pos = dict()
        for i, val in enumerate(a, 1):
            if val not in pos:
                pos[val] = []
            pos[val].append(i)
        
        total_subarrays = n * (n + 1) // 2
        sum_distinct = 0
        
        # For each element, calculate contribution
        for val, indices in pos.items():
            # Add sentinel boundaries
            indices = [0] + indices + [n + 1]
            for i in range(1, len(indices) - 1):
                left = indices[i] - indices[i - 1]
                right = indices[i + 1] - indices[i]
                sum_distinct += left * right
        
        ans = (sum_distinct - total_subarrays) % MOD
        print(ans)

if __name__ == "__main__":
    solve()