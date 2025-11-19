import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    prefix_sum = 0
    max_score = 0
    # We try subsequences formed by the last k elements (k from 1 to N)
    # For each k, average = sum_of_last_k / k
    # score = number of elements > average = number of elements in subsequence strictly greater than average
    # Since subsequence is sorted ascending, elements > average are those strictly greater than average
    # We can find how many elements in the subsequence are > average by binary search or by checking from left
    # But since subsequence is last k elements, and sorted ascending,
    # elements > average are those after the first element > average in the subsequence
    # We can find the count by checking from left to right in the subsequence.
    # But to optimize, we can note that the average is between min and max of subsequence,
    # and since subsequence is sorted, elements > average are those with value > average.
    # So we can find the count by binary search in the subsequence.
    # But since we only consider last k elements, and k can be large, we do a linear approach:
    # For each k, sum_of_last_k = total_sum - prefix_sum_of_first_N-k
    # average = sum_of_last_k / k
    # count elements > average in last k elements: since sorted ascending, find first element > average
    # count = number of elements after that index in last k elements
    # We can do binary search in last k elements to find first element > average.

    # Precompute prefix sums for A
    prefix = [0]
    for v in A:
        prefix.append(prefix[-1] + v)

    # For k in 1..N, consider subsequence = A[N-k..N-1]
    # sum_sub = prefix[N] - prefix[N-k]
    # average = sum_sub / k
    # find first element > average in A[N-k..N-1]
    # count = number of elements > average = number of elements from that index to end of subsequence

    # To speed up, we do binary search for each k
    # Since total N over all T is 2*10^5, O(N log N) per test is acceptable

    from bisect import bisect_right

    max_score = 0
    for k in range(1, N+1):
        sum_sub = prefix[N] - prefix[N - k]
        avg = sum_sub / k
        # find first element > avg in A[N-k..N-1]
        # bisect_right returns insertion point to keep sorted order
        # so first element > avg is at index = bisect_right(A, avg, N-k, N)
        idx = bisect_right(A, avg, N - k, N)
        count = N - idx
        if count > max_score:
            max_score = count

    print(max_score)