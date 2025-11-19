import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0]); M = int(data[1])
    S = data[2].strip()
    MOD = 998244353

    # Precompute integer codes of S
    S_int = [ord(ch) - 97 for ch in S]

    max_state = 1 << N

    # Precompute f_arrays[mask][j] = LCS lengths prefix for DP row
    # where f_arrays[mask][0] = 0, f_arrays[mask][j] = sum of bits mask[0..j-1]
    f_arrays = [[0] * (N + 1) for _ in range(max_state)]
    for mask in range(max_state):
        f = f_arrays[mask]
        # Build prefix sums of mask bits
        s = 0
        for j in range(1, N + 1):
            if (mask >> (j - 1)) & 1:
                s += 1
            f[j] = s

    # Precompute transitions: next_mask[mask][c] -> new mask after adding letter c
    next_mask = [[0] * 26 for _ in range(max_state)]
    for mask in range(max_state):
        f = f_arrays[mask]
        # For each possible new character c
        for c in range(26):
            # Compute updated DP row f_new
            # f_new[0] = 0
            prev = 0  # f_new[j-1]
            m2 = 0
            for j in range(1, N + 1):
                # If S[j-1] matches c
                if S_int[j-1] == c:
                    # match extends from f[j-1]
                    cur = f[j-1] + 1
                else:
                    # no match: take max of f[j] and f_new[j-1]
                    # f[j] = f_arrays[mask][j]
                    fj = f[j]
                    cur = fj if fj >= prev else prev
                # delta = cur - prev; if 1, set bit j-1 in new mask
                if cur - prev:
                    m2 |= (1 << (j - 1))
                prev = cur
            next_mask[mask][c] = m2

    # DP over positions of T
    curr = [0] * max_state
    curr[0] = 1
    for _ in range(M):
        nxt = [0] * max_state
        cm = curr  # alias
        nm = next_mask
        for mask in range(max_state):
            v = cm[mask]
            if v:
                trans = nm[mask]
                # unroll the inner loop a bit
                # for c in range(26):
                #     nxt[trans[c]] = (nxt[trans[c]] + v) % MOD
                # Manual inline for speed
                # But safer to keep simple
                for c in range(26):
                    m2 = trans[c]
                    nxt[m2] = (nxt[m2] + v) % MOD
        curr = nxt

    # Precompute popcounts
    popc = [0] * max_state
    for mask in range(1, max_state):
        popc[mask] = popc[mask >> 1] + (mask & 1)

    # Accumulate answers by popcount of mask
    ans = [0] * (N + 1)
    for mask in range(max_state):
        k = popc[mask]
        ans[k] = (ans[k] + curr[mask]) % MOD

    # Output
    out = " ".join(str(ans[k]) for k in range(N + 1))
    sys.stdout.write(out)

if __name__ == "__main__":
    main()