import sys
sys.setrecursionlimit(100000)
MOD = 998244353

def dfs(state, memo):
    if state in memo:
        return memo[state]
    if len(state) == 0:
        return 1
    if len(state) == 1:
        pos, score = state[0]
        if score is None or score == 0:
            return 1
        else:
            return 0

    total = 0
    n_active = len(state)
    state_list = list(state)
    for i in range(n_active):
        pos_x, score_x = state_list[i]
        if score_x is not None and score_x != 0:
            continue

        candidates = []
        for j in range(n_active):
            if i == j:
                continue
            pos_y, score_y = state_list[j]
            d = abs(pos_x - pos_y)
            candidates.append((d, pos_y, j))
        candidates.sort(key=lambda x: (x[0], x[1]))
        j_index = candidates[0][2]
        pos_y, score_y = state_list[j_index]

        new_state = []
        for k in range(n_active):
            if k == i:
                continue
            pos_k, score_k = state_list[k]
            if k == j_index:
                if score_k is None:
                    new_score = None
                else:
                    new_score = score_k - 1
                new_state.append((pos_k, new_score))
            else:
                new_state.append((pos_k, score_k))

        new_state_sorted = tuple(sorted(new_state, key=lambda x: x[0]))
        total = (total + dfs(new_state_sorted, memo)) % MOD

    memo[state] = total % MOD
    return memo[state]

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        active = []
        for i in range(n):
            if arr[i] == -1:
                active.append((i, None))
            else:
                active.append((i, arr[i]))
        active_tuple = tuple(sorted(active, key=lambda x: x[0]))
        memo = {}
        res = dfs(active_tuple, memo)
        results.append(str(res % MOD))

    print("\n".join(results))

if __name__ == "__main__":
    main()
