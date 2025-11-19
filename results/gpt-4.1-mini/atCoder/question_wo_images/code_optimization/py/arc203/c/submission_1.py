import sys
import threading

MOD = 998244353
MAX = 400005

fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def main():
    input = sys.stdin.readline
    T = int(input())

    # Precompute prefix sums for binomial coefficients for max H and W
    # But since H and W can be up to 2*10^5 and T up to 2*10^5,
    # precomputing for all is not feasible.
    # Instead, we optimize the triple nested loop by using the inclusion-exclusion formula
    # and rewrite the triple sum as a single sum using combinational identities.

    # The original formula is:
    # ans = sum_{j=0}^{H-1} (-1)^j C(H-1, j) * sum_{l=0}^{W-1} (-1)^l C(W-1, l) * C(total_walls - j*W - l*H, K)
    # = sum_{j=0}^{H-1} sum_{l=0}^{W-1} (-1)^{j+l} C(H-1, j) C(W-1, l) C(total_walls - j*W - l*H, K)

    # We can rewrite the double sum as a single sum over s = j + l, but that is complicated.
    # Instead, we can do the double sum efficiently by iterating over the smaller dimension first,
    # and for each fixed j, precompute all C(W-1, l) * (-1)^l and store in a list,
    # then for each l, compute C(total_walls - j*W - l*H, K).

    # But this is still O(H*W) worst case, which is too large.

    # Observation:
    # For fixed K, H, W, the number of terms where C(total_walls - j*W - l*H, K) != 0 is limited,
    # because total_walls - j*W - l*H >= K must hold.
    # So for large j or l, the term is zero.

    # We can limit the loops by the maximum j and l such that total_walls - j*W - l*H >= K.

    # Let's define max_j = min(H-1, (total_walls - K)//W)
    # For each j, max_l = min(W-1, (total_walls - j*W - K)//H)

    # This drastically reduces the number of iterations.

    # We'll implement this approach.

    for _ in range(T):
        H, W, K = map(int, input().split())
        total_walls = 2 * H * W - H - W

        if K > total_walls:
            print(0)
            continue

        max_j = min(H - 1, (total_walls - K) // W)
        ans = 0

        # Precompute C(H-1, j) * (-1)^j for j in [0..max_j]
        cH = [0] * (max_j + 1)
        for j in range(max_j + 1):
            cH[j] = nCr(H - 1, j)
            if j & 1:
                cH[j] = MOD - cH[j]

        # Precompute C(W-1, l) * (-1)^l for l in [0..W-1]
        # But we only need l up to max_l for each j, so we compute on the fly.

        # To speed up, precompute factorials and inverse factorials are already done.

        for j in range(max_j + 1):
            base = total_walls - j * W
            max_l = min(W - 1, (base - K) // H) if base >= K else -1
            if max_l < 0:
                continue

            # Precompute C(W-1, l)*(-1)^l for l in [0..max_l]
            cW = [0] * (max_l + 1)
            for l in range(max_l + 1):
                val = nCr(W - 1, l)
                if l & 1:
                    val = MOD - val
                cW[l] = val

            for l in range(max_l + 1):
                n = base - l * H
                if n < K:
                    break
                ways = nCr(n, K)
                term = cH[j] * cW[l] % MOD * ways % MOD
                ans = (ans + term) % MOD

        print(ans)

threading.Thread(target=main).start()