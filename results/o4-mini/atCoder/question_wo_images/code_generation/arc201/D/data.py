import sys
import bisect

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    # We want to minimize max((A_i + B_i) % M)
    # For each B_i, we want to find A_j such that (A_j + B_i) % M is as small as possible.
    # This is equivalent to finding A_j >= (M - B_i) mod M to get sum mod M close to 0.
    # If no such A_j, take the smallest A_j.

    # We'll use a sorted list of A and remove elements as we assign them.
    # Since sum of N is large, we need efficient removal.
    # Use a balanced approach with bisect and a pointer.

    # Instead of removing elements from A, we can use a pointer approach:
    # But we need to assign each A_j exactly once.
    # So we can use a balanced data structure or simulate with a list and bisect.

    # Since we need to remove elements, we can use a balanced tree structure.
    # Python doesn't have built-in balanced tree, but we can use a trick:
    # Use a list and maintain a pointer for the smallest element.
    # For each B_i, we binary search for the smallest A_j >= (M - B_i).
    # If found, assign and remove that element.
    # Else assign the smallest element.

    # To efficiently remove elements, we can use a multiset approach with a balanced tree.
    # But since sum of N is large, we need O(N log N) solution.

    # We'll use a sorted list and for each B_i:
    # - binary search for A_j >= (M - B_i)
    # - if found, pop that element
    # - else pop the smallest element (A[0])

    # To efficiently remove elements, we can use a balanced tree structure.
    # Since Python doesn't have one, we can use the "sortedcontainers" module,
    # but it's not allowed here.
    # So we implement a balanced tree using bisect and a list.

    # We'll implement a balanced tree using a list and bisect.
    # For each removal, we do O(log N).

    # This is acceptable for sum of N up to 3*10^5.

    from bisect import bisect_left

    A_list = A[:]  # copy
    res = 0
    for b in B:
        target = (M - b) % M
        idx = bisect_left(A_list, target)
        if idx == len(A_list):
            # no element >= target, take smallest
            a = A_list.pop(0)
        else:
            a = A_list.pop(idx)
        val = (a + b) % M
        if val > res:
            res = val
    print(res)