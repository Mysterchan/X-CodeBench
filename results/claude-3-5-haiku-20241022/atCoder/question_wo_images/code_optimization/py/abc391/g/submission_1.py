N, M = map(int, input().split())
S = input().strip()
mod = 998244353

# Precompute positions of each character in S
char_pos = [[] for _ in range(26)]
for i, c in enumerate(S):
    char_pos[ord(c) - ord('a')].append(i)

# DP: state = tuple of LCS lengths for each prefix of S
D = {(0,) * (N + 1): 1}

for _ in range(M):
    DD = {}
    for state, count in D.items():
        # For each character we can append
        for ch in range(26):
            # Compute new state
            new_state = [0] * (N + 1)
            for k in range(N):
                new_state[k + 1] = max(new_state[k], state[k + 1])
                if S[k] == chr(ch + ord('a')):
                    new_state[k + 1] = max(new_state[k + 1], state[k] + 1)
            
            key = tuple(new_state)
            DD[key] = (DD.get(key, 0) + count) % mod
    
    D = DD

# Collect answers
ans = [0] * (N + 1)
for state, count in D.items():
    ans[state[-1]] = (ans[state[-1]] + count) % mod

print(*ans)