import sys

MOD = 998244353

def solve():
    N = int(sys.stdin.readline())
    A = []
    for _ in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))

    if N == 1:
        print(1)
        return

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    C = [set() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                C[i].add(j)

    C_frozen = [frozenset(s) for s in C]

    for i in range(N):
        if 0 not in C[i]:
            print(0)
            return

    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] == 1:
                if not (C_frozen[i].issubset(C_frozen[j]) or C_frozen[j].issubset(C_frozen[i])):
                    print(0)
                    return

    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if k == i or k == j: continue
                if A[i][j] == 1 and A[j][k] == 1 and A[i][k] == 0:

                    if not (C_frozen[i].issubset(C_frozen[j]) and C_frozen[k].issubset(C_frozen[j])):
                        print(0)
                        return

    groups = {}
    for i in range(N):
        s_frozen = C_frozen[i]
        if s_frozen not in groups:
            groups[s_frozen] = []
        groups[s_frozen].append(i)

    for s_val_set, group_nodes in groups.items():
        for r in range(len(group_nodes)):
            for c in range(r + 1, len(group_nodes)):
                u, v = group_nodes[r], group_nodes[c]
                if A[u][v] == 0:
                    print(0)
                    return

    ans = 1
    c0_frozen = C_frozen[0]

    for s_val_set, group_nodes in groups.items():
        count = len(group_nodes)
        if s_val_set == c0_frozen:
            ans = (ans * fact[count - 1]) % MOD
        else:
            ans = (ans * fact[count]) % MOD

    print(ans)

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()