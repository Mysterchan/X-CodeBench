import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    maxA = 10**6

    freq = [0] * (maxA + 1)
    for v in A:
        freq[v] += 1

    # cnt[d]: how many elements in A are divisible by d
    cnt = [0] * (maxA + 1)
    for d in range(1, maxA + 1):
        s = 0
        for multiple in range(d, maxA + 1, d):
            s += freq[multiple]
        cnt[d] = s

    # For each d, if cnt[d] >= K, then d is a candidate gcd
    # We want to find for each A[i], the maximum d dividing A[i] with cnt[d] >= K

    # Precompute divisors for each number up to maxA
    # To optimize, we can precompute divisors for all numbers using a sieve approach
    divisors = [[] for _ in range(maxA + 1)]
    for d in range(1, maxA + 1):
        for multiple in range(d, maxA + 1, d):
            divisors[multiple].append(d)

    res = [1] * N
    for i in range(N):
        best = 1
        for d in divisors[A[i]]:
            if cnt[d] >= K and d > best:
                best = d
        res[i] = best

    print('\n'.join(map(str, res)))

threading.Thread(target=main).start()