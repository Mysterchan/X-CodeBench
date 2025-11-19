import sys
import threading

def main():
    import math
    data = sys.stdin.read().strip()
    if not data:
        return
    R = int(data)
    R2_4 = 4 * R * R
    ans = 0
    # Loop over non-negative A = |i|
    # For each A, find max B = |j| such that (A+0.5)^2 + (B+0.5)^2 <= R^2
    for A in range(0, R):
        v = 2 * A + 1
        T = R2_4 - v * v
        if T < 0:
            break
        # 2*B+1 <= sqrt(T)  => B_max = (floor(sqrt(T)) - 1) // 2
        t = math.isqrt(T)
        Bmax = (t - 1) // 2
        # sum of mult(B) for B=0..Bmax = 1 + 2*Bmax
        sum_mult_j = 1 + 2 * Bmax
        # mult(A) = 1 if A==0 else 2
        multA = 1 if A == 0 else 2
        ans += multA * sum_mult_j

    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()