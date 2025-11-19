import sys

MOD = 998244353

def solve():

    N, Q = map(int, sys.stdin.readline().split())

    A_input = list(map(int, sys.stdin.readline().split()))

    A = [0] * (N + 1)
    for i in range(2, N + 1):

        if i-2 < len(A_input):
            A[i] = A_input[i-2]
        else:

             pass

    fact_N_minus_1 = 1

    if N > 1:
        for i in range(1, N):
            fact_N_minus_1 = (fact_N_minus_1 * i) % MOD

    inv = [0] * (N + 1)
    if N >= 1: inv[1] = 1
    if N >= 2:

        for i in range(2, N + 1):
           inv[i] = (MOD - (MOD // i) * inv[MOD % i]) % MOD

    PS1 = [0] * (N + 1)

    PS2 = [0] * (N + 1)

    for k in range(2, N + 1):

        current_A_k = A[k] % MOD

        term1 = (current_A_k * inv[k]) % MOD

        PS1[k] = (PS1[k-1] + term1) % MOD

        term2 = current_A_k

        PS2[k] = (PS2[k-1] + term2) % MOD

    results = []

    for _ in range(Q):

        u, v = map(int, sys.stdin.readline().split())

        term_Du_over_F = 0
        if u >= 2:

             current_A_u = A[u] % MOD
             term_Du_over_F = (PS1[u-1] + current_A_u) % MOD

        term_Dv_over_F = 0

        if v >= 2:

             current_A_v = A[v] % MOD
             term_Dv_over_F = (PS1[v-1] + current_A_v) % MOD

        term_Tuv_over_F = 0
        if u >= 2:

             term_Tuv_over_F = (inv[u] * PS2[u]) % MOD

        two_times_Tuv_over_F = (2 * term_Tuv_over_F) % MOD
        total_inner = (term_Du_over_F + term_Dv_over_F - two_times_Tuv_over_F + MOD) % MOD

        ans = (fact_N_minus_1 * total_inner) % MOD

        results.append(ans)

    sys.stdout.write("\n".join(map(str, results)) + "\n")

solve()