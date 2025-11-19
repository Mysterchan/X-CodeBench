import sys

MOD = 998244353

def solve():
    N = int(sys.stdin.readline())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    if N == 1:
        print(1)
        return

    # Pre-compute factorials
    fact = [1] * (N + 1)
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    # Check conditions for trees
    ancestor_sets = [set() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                ancestor_sets[i].add(j)

    # Condition 1: Vertex 1 must be an ancestor to all others
    if not (0 in ancestor_sets[0]):
        print(0)
        return

    # Group the nodes by their ancestor sets
    groups = {}
    for i in range(N):
        frozen_set = frozenset(ancestor_sets[i])
        if frozen_set not in groups:
            groups[frozen_set] = []
        groups[frozen_set].append(i)

    # Validate ancestor property
    for ancestor_set, group in groups.items():
        for i in group:
            for j in group:
                if i != j and not A[i][j]:
                    print(0)
                    return

    ans = 1
    c0_count = len(groups[frozenset(ancestor_sets[0])]) - 1

    # Count valid trees
    for frozen_set, group in groups.items():
        group_size = len(group)
        if frozen_set == frozenset(ancestor_sets[0]):
            ans = (ans * fact[group_size]) % MOD
        else:
            ans = (ans * fact[group_size]) % MOD

    print(ans)

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()