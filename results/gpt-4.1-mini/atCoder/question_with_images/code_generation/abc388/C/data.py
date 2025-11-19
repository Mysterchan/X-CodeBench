import sys
import bisect

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    for i in range(N):
        # For mochi A[i] as the top mochi (size a),
        # find how many mochi B (size b) satisfy a <= b/2
        # i.e. b >= 2*a
        # Since A is sorted ascending, find the first index j where A[j] >= 2*A[i]
        # All mochi from j to N-1 can be bottom mochi for top mochi i
        j = bisect.bisect_left(A, 2 * A[i])
        count += N - j

    print(count)

if __name__ == "__main__":
    main()