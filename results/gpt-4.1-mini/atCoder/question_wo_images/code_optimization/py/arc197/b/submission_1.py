def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()

        prefix_sum = 0
        ans = 0
        for i in range(N):
            prefix_sum += A[i]
            # average = prefix_sum / (i+1)
            # number of elements > average = count of elements in A[:i+1] strictly greater than average
            # Since A is sorted, elements > average start from index bisect_right(A[:i+1], average)
            # Instead of bisect, we can do a binary search manually or use bisect module efficiently
            # But since we only need to find the first element > average in A[:i+1], and A[:i+1] is sorted,
            # we can use bisect_right directly on A with a slice or on A[:i+1].
            # To avoid slicing overhead, use bisect_right on A with range [0, i+1)
            # bisect_right(A, average, 0, i+1)
            from bisect import bisect_right
            ave = prefix_sum / (i + 1)
            pos = bisect_right(A, ave, 0, i + 1)
            tmp = (i + 1) - pos
            if tmp > ans:
                ans = tmp
        print(ans)