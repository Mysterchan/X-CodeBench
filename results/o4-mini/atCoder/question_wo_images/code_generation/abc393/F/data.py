import sys
import threading

def main():
    import sys
    from bisect import bisect_left, bisect_right

    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    queries = []
    for idx in range(q):
        r = int(next(it))
        x = int(next(it))
        queries.append((r, x, idx))

    # Sort queries by their R-value (prefix length)
    queries.sort(key=lambda t: t[0])

    tail = []            # tail[k] = minimum ending value of an increasing subsequence of length k+1
    answers = [0] * q
    qi = 0               # pointer into sorted queries

    for i in range(1, n + 1):
        ai = A[i-1]
        # Update the patience sorting "tail" array
        pos = bisect_left(tail, ai)
        if pos == len(tail):
            tail.append(ai)
        else:
            tail[pos] = ai

        # Answer all queries with R == i
        while qi < q and queries[qi][0] == i:
            _, x, orig_idx = queries[qi]
            # The answer is the largest k such that tail[k-1] <= x,
            # which is bisect_right(tail, x).
            ans = bisect_right(tail, x)
            answers[orig_idx] = ans
            qi += 1

    # Output in the original query order
    out = '\n'.join(map(str, answers))
    sys.stdout.write(out)

if __name__ == "__main__":
    main()