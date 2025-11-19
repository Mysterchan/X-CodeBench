import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    data = sys.stdin.read().split()
    N = int(data[0]); M = int(data[1])
    S = data[2]
    # total strings
    total = pow(26, M, MOD)
    # g[k]: number of strings T with LCS(S,T) < k
    # for k=1: LCS<1 means no common letter => letters outside S only
    uniq = len(set(S))
    g = [0] * (N + 2)
    g[1] = pow(26 - uniq, M, MOD)
    # precompute S as list of ints 0..25
    S_int = [ord(c) - 97 for c in S]
    # For k = 2..N, do DP avoiding masks with popcount >= k
    for k in range(2, N + 1):
        # collect masks with popcount <= k-1
        masks = []
        for m in range(1 << N):
            if m.bit_count() <= k - 1:
                masks.append(m)
        M_cnt = len(masks)
        # map mask -> idx
        idx_of = {m: i for i, m in enumerate(masks)}
        # precompute dp_old for each mask: dp_old[j] = LCS length up to S[0..j-1]
        dp_old_list = [None] * M_cnt
        for i, m in enumerate(masks):
            dp = [0] * (N + 1)
            # dp[j] = dp[j-1] + bit of m at j-1
            cnt = 0
            for j in range(1, N + 1):
                if (m >> (j - 1)) & 1:
                    cnt += 1
                dp[j] = cnt
            dp_old_list[i] = dp
        # build transitions: for each state i, list of (next_idx, count)
        trans = [None] * M_cnt
        for i, m in enumerate(masks):
            dp_old = dp_old_list[i]
            cnts = {}
            # for each letter 0..25
            for c in range(26):
                # compute dp_new
                dpn = [0] * (N + 1)
                # dpn[0]=0
                for j in range(1, N + 1):
                    v1 = dp_old[j]
                    v2 = dpn[j - 1]
                    if S_int[j - 1] == c:
                        v3 = dp_old[j - 1] + 1
                        # v3 >= 1
                        if v3 >= v1 and v3 >= v2:
                            dpj = v3
                        else:
                            dpj = v1 if v1 >= v2 else v2
                    else:
                        # no match
                        dpj = v1 if v1 >= v2 else v2
                    dpn[j] = dpj
                # build new mask
                nm = 0
                for j in range(1, N + 1):
                    if dpn[j] == dpn[j - 1] + 1:
                        nm |= 1 << (j - 1)
                # check popcount
                if nm.bit_count() <= k - 1:
                    jidx = idx_of[nm]
                    cnts[jidx] = cnts.get(jidx, 0) + 1
            # store transitions
            trans[i] = list(cnts.items())
        # DP over length M
        dp_cur = [0] * M_cnt
        dp_cur[0] = 1  # start from mask=0
        for _ in range(M):
            dp_nxt = [0] * M_cnt
            for i in range(M_cnt):
                v = dp_cur[i]
                if v:
                    for jidx, c in trans[i]:
                        dp_nxt[jidx] = (dp_nxt[jidx] + v * c) % MOD
            dp_cur = dp_nxt
        g[k] = sum(dp_cur) % MOD
    # compute answers ans[0..N]
    ans = [0] * (N + 1)
    # ans[0]: LCS exactly 0 => g[1]
    ans[0] = g[1]
    # ans[k] = g[k+1] - g[k]
    for k in range(1, N):
        ans[k] = (g[k + 1] - g[k]) % MOD
    # ans[N] = total - g[N]
    ans[N] = (total - g[N]) % MOD
    # output
    print(" ".join(str(ans[i]) for i in range(N + 1)))

if __name__ == "__main__":
    main()