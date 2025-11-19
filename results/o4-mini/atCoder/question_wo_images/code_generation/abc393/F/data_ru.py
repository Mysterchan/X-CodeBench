import sys
import threading

def main():
    import sys
    from bisect import bisect_left, bisect_right

    readline = sys.stdin.readline
    N, Q = map(int, readline().split())
    A = list(map(int, readline().split()))

    # Group queries by their R-value (0-based index)
    queries = [[] for _ in range(N)]
    for qi in range(Q):
        r, x = map(int, readline().split())
        queries[r-1].append((qi, x))

    # tails[k] = the minimum ending value of any strictly increasing subsequence of length k+1
    tails = []
    ans = [0] * Q

    for i in range(N):
        ai = A[i]
        # Insert ai into tails: find the place to replace or extend
        pos = bisect_left(tails, ai)
        if pos == len(tails):
            tails.append(ai)
        else:
            tails[pos] = ai

        # Answer all queries with R = i+1
        for qi, x in queries[i]:
            # We need the maximum k such that tails[k-1] <= x
            # bisect_right gives us the count of elements <= x
            ans[qi] = bisect_right(tails, x)

    # Output answers
    out = sys.stdout
    for v in ans:
        out.write(str(v) + "\n")

if __name__ == "__main__":
    main()