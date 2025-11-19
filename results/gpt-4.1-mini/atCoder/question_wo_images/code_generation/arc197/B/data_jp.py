import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    prefix_sum = [0]
    for v in A:
        prefix_sum.append(prefix_sum[-1] + v)

    max_score = 0
    # We try to find the maximum k (number of elements greater than average)
    # by checking suffixes of length k.
    # For each k, check if the average of the subsequence formed by
    # the smallest N-k elements plus the k largest elements is less than
    # the smallest element in the k largest elements.
    # This ensures all k largest elements are greater than the average.
    for k in range(1, N+1):
        total = prefix_sum[N-k] + prefix_sum[N] - prefix_sum[N-k]
        length = N - k + k
        avg = total / length
        # The smallest element in the k largest elements is A[N-k]
        if A[N-k] > avg:
            max_score = k
        else:
            # Since A is sorted ascending, if this k fails,
            # larger k will also fail.
            break

    print(max_score)