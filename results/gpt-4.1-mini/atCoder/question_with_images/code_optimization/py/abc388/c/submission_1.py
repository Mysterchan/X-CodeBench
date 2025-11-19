import sys
import bisect

def solve(N, A):
    ans = 0
    for i in range(N):
        a = A[i]
        # Find the smallest index j > i where A[j] >= 2*a
        j = bisect.bisect_left(A, 2*a, i+1, N)
        if j < N:
            ans += N - j
    return ans

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

if __name__ == "__main__":
    main()