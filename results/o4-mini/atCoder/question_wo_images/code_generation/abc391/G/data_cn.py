import sys
import threading

def main():
    import sys
    data = sys.stdin.read().strip().split()
    N = int(data[0]); M = int(data[1])
    S = data[2]
    mod = 998244353

    # All possible masks: 0..2^N -1
    S_states = 1 << N

    # Precompute f_list[mask][i]: LCS length with S-prefix i and some T,
    # but here simply prefix sums of bits of mask.
    # f_list[mask][0] = 0, f_list[mask][i] = popcount of mask's low i bits.
    f_list = [[0] * (N + 1) for _ in range(S_states)]
    for mask in range(S_states):
        # build prefix sums
        for i in range(1, N+1):
            f_list[mask][i] = f_list[mask][i-1] + ((mask >> (i-1)) & 1)

    # Unique characters in S
    uniq_chars = list(set(S))
    K = len(uniq_chars)
    mismatch_count = 26 - K

    # Precompute transitions: for each mask, list of (next_mask, count_of_chars)
    # that cause the transition.
    trans = [[] for _ in range(S_states)]
    for mask in range(S_states):
        f = f_list[mask]
        # build a temporary dict from next_mask -> count
        d = {}
        # mismatch letters all send to same next mask = mask
        if mismatch_count:
            d[mask] = mismatch_count

        # For each character c in S, compute the next mask
        for c in uniq_chars:
            # compute g array for one more T-character = c
            g0 = 0
            new_mask = 0
            # We'll compute g[i] on the fly and compare to g[i-1]
            # Maintain prev_g = g[i-1]
            prev_g = 0
            for i in range(1, N+1):
                # f[i], prev_g, and candidate = f[i-1] + (S[i-1]==c)
                # match?
                if S[i-1] == c:
                    cand = f[i-1] + 1
                else:
                    cand = -1  # so it won't win unless both f[i], prev_g are negative
                # now new g[i]
                # we know f[i] >= 0 and prev_g >= 0, so taking max is safe
                if f[i] >= prev_g:
                    if f[i] >= cand:
                        gi = f[i]
                    else:
                        gi = cand
                else:
                    if prev_g >= cand:
                        gi = prev_g
                    else:
                        gi = cand
                # if gi > prev_g, then g[i] > g[i-1], we set bit i-1
                if gi > prev_g:
                    new_mask |= (1 << (i-1))
                prev_g = gi
            # record transition
            d[new_mask] = d.get(new_mask, 0) + 1

        # store as list
        trans[mask] = list(d.items())

    # DP over T-length M
    dp = [0] * S_states
    dp[0] = 1
    for _ in range(M):
        ndp = [0] * S_states
        for m in range(S_states):
            v = dp[m]
            if v:
                for m2, cnt in trans[m]:
                    ndp[m2] = (ndp[m2] + v * cnt) % mod
        dp = ndp

    # Collect answers by popcount of mask
    ans = [0] * (N + 1)
    for mask in range(S_states):
        k = f_list[mask][N]  # popcount up to N
        ans[k] = (ans[k] + dp[mask]) % mod

    # print
    print(" ".join(str(ans[k]) for k in range(N+1)))

if __name__ == "__main__":
    main()