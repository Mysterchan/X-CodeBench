import sys
import threading
import bisect

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        A.sort()
        ts = 0
        ans = 0
        for i, v in enumerate(A):
            ts += v
            # find number of elements in A[0..i] strictly greater than average ts/(i+1)
            # use bisect_right on the sorted prefix without slicing
            pos = bisect.bisect_right(A, ts / (i + 1), 0, i + 1)
            cnt = (i + 1) - pos
            if cnt > ans:
                ans = cnt
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()