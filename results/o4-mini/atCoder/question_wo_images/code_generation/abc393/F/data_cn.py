import sys
import threading
def main():
    import sys
    from bisect import bisect_left, bisect_right

    data = sys.stdin.readline().split()
    if not data:
        return
    N = int(data[0]); Q = int(data[1])
    A = list(map(int, sys.stdin.readline().split()))
    queries = []
    for qi in range(Q):
        line = sys.stdin.readline().split()
        r = int(line[0]); x = int(line[1])
        queries.append((r, x, qi))
    # Sort queries by R
    queries.sort(key=lambda t: t[0])
    ans = [0] * Q
    dp = []
    ptr = 0
    for i in range(1, N+1):
        a = A[i-1]
        # LIS dp update: find position to place a
        pos = bisect_left(dp, a)
        if pos == len(dp):
            dp.append(a)
        else:
            dp[pos] = a
        # process queries with R == i
        while ptr < Q and queries[ptr][0] == i:
            _, x, idx = queries[ptr]
            # answer is number of dp entries <= x
            res = bisect_right(dp, x)
            ans[idx] = res
            ptr += 1
    # Output answers
    out = sys.stdout
    for v in ans:
        out.write(str(v))
        out.write('\n')

if __name__ == "__main__":
    main()