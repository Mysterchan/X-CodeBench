import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    mod = 998244353

    N = int(next(it))
    Q = int(next(it))
    # Read weights A_2 ... A_N
    A = [int(next(it)) for _ in range(N-1)]

    # Precompute inverses up to N+1
    inv = [0] * (N+2)
    inv[1] = 1
    for i in range(2, N+2):
        # inv[i] = pow(i, mod-2, mod)  # slower
        inv[i] = mod - (mod//i) * inv[mod % i] % mod

    # Precompute factorial (N-1)!
    fact = 1
    for i in range(1, N):
        fact = fact * i % mod
    factN1 = fact  # (N-1)!

    # Build prefix sums:
    # pre2[x] = sum_{i=2..x} inv(i) * A[i-2]
    # pre1[x] = sum_{i=2..x} 2*(i-1)/(i*(i+1)) * A[i-2]
    pre2 = [0] * (N+2)
    pre1 = [0] * (N+2)

    for x in range(2, N+1):
        ai = A[x-2]  # weight A_x
        # update pre2
        v2 = ai * inv[x] % mod
        pre2[x] = pre2[x-1] + v2
        if pre2[x] >= mod:
            pre2[x] -= mod

        # update pre1
        # weight1 = 2*(x-1) * inv[x] * inv[x+1] % mod
        w1 = (2*(x-1)) % mod
        w1 = w1 * inv[x] % mod
        w1 = w1 * inv[x+1] % mod
        v1 = ai * w1 % mod
        pre1[x] = pre1[x-1] + v1
        if pre1[x] >= mod:
            pre1[x] -= mod

    out = []
    for _ in range(Q):
        a = int(next(it))
        b = int(next(it))
        # sum1 = sum_{i=2..a-1} 2*(i-1)/(i*(i+1)) * A[i-2]
        sum1 = pre1[a-1]
        # sum2 = (a-1)/a * A[a-2], but zero if a==1
        if a > 1:
            sum2 = (a-1) * inv[a] % mod * A[a-2] % mod
        else:
            sum2 = 0
        # sum3 = sum_{i=a+1..b-1} inv(i)*A[i-2]
        # = pre2[b-1] - pre2[a]
        sum3 = pre2[b-1] - pre2[a]
        if sum3 < 0:
            sum3 += mod
        # sum4 = A[b-2]
        sum4 = A[b-2]

        s = sum1 + sum2
        if s >= mod: s -= mod
        s += sum3
        if s >= mod: s -= mod
        s += sum4
        if s >= mod: s -= mod

        ans = s * factN1 % mod
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()