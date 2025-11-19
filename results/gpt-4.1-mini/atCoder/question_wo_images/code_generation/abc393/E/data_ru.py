import sys
import threading

def main():
    import sys
    import math

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    MAX_A = 10**6

    freq = [0]*(MAX_A+1)
    for x in A:
        freq[x] += 1

    # cnt[d] = how many elements in A are divisible by d
    cnt = [0]*(MAX_A+1)
    for d in range(1, MAX_A+1):
        s = 0
        for multiple in range(d, MAX_A+1, d):
            s += freq[multiple]
        cnt[d] = s

    # For each d, if cnt[d] >= K, then d is a candidate gcd for some K elements

    # For each element A[i], we want to find the maximum d dividing A[i] with cnt[d]>=K

    # To do this efficiently, we precompute divisors for each A[i] on the fly.

    # Since MAX_A=1e6, we can precompute smallest prime factor (spf) for factorization

    spf = [0]*(MAX_A+1)
    for i in range(2, MAX_A+1):
        if spf[i] == 0:
            for j in range(i, MAX_A+1, i):
                if spf[j] == 0:
                    spf[j] = i

    def get_divisors(x):
        # get prime factorization
        pf = []
        while x > 1:
            p = spf[x]
            cnt_p = 0
            while x % p == 0:
                x //= p
                cnt_p += 1
            pf.append((p, cnt_p))
        # generate divisors from prime factors
        divisors = [1]
        for p, c in pf:
            new_divs = []
            for d in divisors:
                val = d
                for _ in range(c):
                    val *= p
                    new_divs.append(val)
            divisors += new_divs
        return divisors

    # For each A[i], find max divisor d with cnt[d]>=K
    # Since divisors are generated, we check cnt[d] and keep max

    output = [0]*N
    for i in range(N):
        divisors = get_divisors(A[i])
        max_d = 1
        for d in divisors:
            if cnt[d] >= K and d > max_d:
                max_d = d
        output[i] = max_d

    print('\n'.join(map(str, output)))

threading.Thread(target=main).start()