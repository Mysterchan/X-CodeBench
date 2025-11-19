import sys
import threading
def main():
    import sys
    input = sys.stdin.readline
    mod = 998244353

    N, M = map(int, input().split())
    S_str = input().strip()
    # Precompute a bitmask for each letter: which positions in S match that letter
    char_mask = [0] * 26
    for i, ch in enumerate(S_str):
        char_mask[ord(ch) - 97] |= 1 << i

    # Number of states is 2^N (bitmask of length N)
    bits = 1 << N
    full_mask = bits - 1

    # Precompute transition for each state and each letter j in [0..25]
    # Then group by target state to count how many letters map to that target.
    transitions = [None] * bits
    for st in range(bits):
        cnts = {}
        # 'st' is the current bitmask state
        for j in range(26):
            m = char_mask[j]
            x = m | st
            y = ((st << 1) | 1)
            # compute new state v
            v = x & (x ^ (x - y))
            v &= full_mask
            cnts[v] = cnts.get(v, 0) + 1
        # store as list of (target_state, count_of_letters)
        transitions[st] = list(cnts.items())

    # DP array: dp[st] = number of strings of current length ending in state st
    dp = [0] * bits
    dp[0] = 1

    for _ in range(M):
        new_dp = [0] * bits
        for st in range(bits):
            c = dp[st]
            if c:
                for to_st, cnt_letters in transitions[st]:
                    new_dp[to_st] = (new_dp[to_st] + c * cnt_letters) % mod
        dp = new_dp

    # Precompute popcounts for all states
    popc = [0] * bits
    for st in range(1, bits):
        popc[st] = popc[st >> 1] + (st & 1)

    # Aggregate answers by popcount = LCS length
    ans = [0] * (N + 1)
    for st in range(bits):
        k = popc[st]
        ans[k] = (ans[k] + dp[st]) % mod

    print(*ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()