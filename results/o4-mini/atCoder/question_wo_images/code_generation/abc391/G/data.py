import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    mod = 998244353

    N, M = map(int, sys.stdin.readline().split())
    S_str = sys.stdin.readline().strip()
    # Convert S to list of ints 0..25
    S = [ord(c) - ord('a') for c in S_str]

    # Number of states: 2^N
    SIZ = 1 << N

    # Precompute transitions: next_state[state][c] = new_state
    next_state = [[0] * 26 for _ in range(SIZ)]

    # For each state mask, compute its dp[0..N], then for each c, compute newmask
    for mask in range(SIZ):
        # Reconstruct dp[0..N] from mask bits: dp[j] = sum_{t=1..j} bit t
        dp = [0] * (N + 1)
        for j in range(1, N + 1):
            dp[j] = dp[j - 1] + ((mask >> (j - 1)) & 1)
        # For each character c
        for c in range(26):
            newdp = [0] * (N + 1)
            # newdp[0] = 0
            for j in range(1, N + 1):
                # if S[j-1] matches c
                if S[j - 1] == c:
                    # we can extend from dp[j-1]
                    v = dp[j - 1] + 1
                else:
                    # we take max(dp[j], newdp[j-1])
                    v = dp[j] if dp[j] >= newdp[j - 1] else newdp[j - 1]
                newdp[j] = v
            # Build newmask from newdp bits
            nm = 0
            for j in range(1, N + 1):
                if newdp[j] - newdp[j - 1] == 1:
                    nm |= 1 << (j - 1)
            next_state[mask][c] = nm

    # DP arrays: curr_dp[state] = count of strings of current length leading to 'state'
    curr_dp = [0] * SIZ
    curr_dp[0] = 1  # empty T, dp is all zeros => mask=0

    # Iterate over positions 1..M
    for _ in range(M):
        nxt_dp = [0] * SIZ
        # For each state with non-zero count
        for mask in range(SIZ):
            cnt = curr_dp[mask]
            if cnt:
                # Try all 26 letters
                # speed: localize
                nst = next_state[mask]
                for c in range(26):
                    nm = nst[c]
                    nxt_dp[nm] = (nxt_dp[nm] + cnt) % mod
        curr_dp = nxt_dp

    # Now curr_dp[state] has counts for all T of length M
    # ans[k] = sum of curr_dp[mask] where popcount(mask) == k
    ans = [0] * (N + 1)
    # Precompute popcounts
    popcnt = [0] * SIZ
    for m in range(1, SIZ):
        popcnt[m] = popcnt[m >> 1] + (m & 1)
    for mask in range(SIZ):
        k = popcnt[mask]
        ans[k] = (ans[k] + curr_dp[mask]) % mod

    # Output ans[0..N]
    print(" ".join(str(ans[k]) for k in range(N + 1)))

if __name__ == "__main__":
    main()