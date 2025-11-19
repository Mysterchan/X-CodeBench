MOD = 998244353

import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    parts = data[0].split()
    N_val = int(parts[0])
    M_val = int(parts[1])
    S = data[1].strip()
    N = N_val
    M = M_val

    if N == 0:
        total = pow(26, M, MOD)
        print(total)
        return

    total_masks = 1 << N
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    trans = [[0] * 26 for _ in range(total_masks)]

    for mask in range(total_masks):
        prev_x = [0] * (N + 1)
        for j in range(1, N + 1):
            mask_j = mask & ((1 << j) - 1)
            prev_x[j] = bin(mask_j).count('1')

        for idx, c in enumerate(alphabet):
            new_vector = [0] * (N + 1)
            for j in range(1, N + 1):
                base = max(prev_x[j], new_vector[j - 1])
                if S[j - 1] == c:
                    candidate = prev_x[j - 1] + 1
                    if candidate > base:
                        new_vector[j] = candidate
                    else:
                        new_vector[j] = base
                else:
                    new_vector[j] = base
            new_mask = 0
            for j in range(0, N):
                if new_vector[j + 1] - new_vector[j] == 1:
                    new_mask |= (1 << j)
            trans[mask][idx] = new_mask

    dp = [0] * total_masks
    dp[0] = 1

    for _ in range(M):
        new_dp = [0] * total_masks
        for mask in range(total_masks):
            cnt = dp[mask]
            if cnt == 0:
                continue
            for c_index in range(26):
                next_mask = trans[mask][c_index]
                new_dp[next_mask] = (new_dp[next_mask] + cnt) % MOD
        dp = new_dp

    ans = [0] * (N + 1)
    for mask in range(total_masks):
        k_val = bin(mask).count('1')
        if k_val <= N:
            ans[k_val] = (ans[k_val] + dp[mask]) % MOD

    print(" ".join(str(x) for x in ans))

if __name__ == '__main__':
    main()