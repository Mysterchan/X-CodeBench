import sys
import threading

def main():
    import sys
    from array import array

    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    # Read A values
    A = [0] * n
    maxA = 0
    for i in range(n):
        v = int(next(it))
        A[i] = v
        if v > maxA:
            maxA = v
    # Build count array
    cnt = array('I', [0]) * (maxA + 1)
    for v in A:
        cnt[v] += 1
    # Build freq array: freq[d] = number of A's divisible by d
    freq = array('I', [0]) * (maxA + 1)
    # Sieve multiples
    for d in range(1, maxA + 1):
        c = 0
        # sum cnt[m] for m = d, 2d, 3d, ...
        for m in range(d, maxA + 1, d):
            c += cnt[m]
        freq[d] = c
    # Build smallest-prime-factor (spf) array up to maxA
    spf = array('I', [0]) * (maxA + 1)
    if maxA >= 1:
        spf[1] = 1
    import math
    for i in range(2, maxA + 1):
        if spf[i] == 0:
            # i is prime
            spf[i] = i
            step = i
            # mark spf for multiples
            for j in range(i * 2, maxA + 1, step):
                if spf[j] == 0:
                    spf[j] = i

    out = sys.stdout.write
    # For each A[i], factorize, generate divisors, pick max d with freq[d] >= k
    for v in A:
        # factorize v by spf
        tmp = v
        pf = []
        while tmp > 1:
            p = spf[tmp]
            cntp = 0
            # count exponent
            while tmp % p == 0:
                tmp //= p
                cntp += 1
            pf.append((p, cntp))
        # generate all divisors
        divs = [1]
        for (p, e) in pf:
            base_len = len(divs)
            # for each existing divisor, multiply by p^1, p^2, ..., p^e
            mul = p
            for _ in range(e):
                for j in range(base_len):
                    divs.append(divs[j] * mul)
                mul *= p
        # find maximum valid divisor
        best = 1
        # freq[1] >= k always since K <= N
        for d in divs:
            # check
            if d > best and freq[d] >= k:
                best = d
        out(str(best))
        out('\n')

if __name__ == "__main__":
    main()