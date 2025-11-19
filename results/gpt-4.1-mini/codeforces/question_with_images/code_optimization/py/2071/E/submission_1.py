import sys
MOD = 998244353
inv2 = (MOD + 1) // 2

def modinv(x):
    return pow(x, MOD - 2, MOD)

def main():
    input = sys.stdin.readline
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        p_list = [0] * (n + 1)
        q_list = [0] * (n + 1)
        for i in range(1, n + 1):
            pi, qi = map(int, input().split())
            p_list[i] = pi
            q_list[i] = qi

        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = p_list[i] * modinv(q_list[i]) % MOD

        graph = [[] for _ in range(n + 1)]
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            if u < v:
                edges.append((u, v))
            else:
                edges.append((v, u))

        # Precompute P[u] = product of a[v] for all neighbors v of u
        # and R[u] = sum over neighbors v of (1 - a[v]) / a[v]
        P = [1] * (n + 1)
        R = [0] * (n + 1)
        for u in range(1, n + 1):
            prod = 1
            total = 0
            for v in graph[u]:
                av = a[v]
                prod = (prod * av) % MOD
            P[u] = prod
        for u in range(1, n + 1):
            total = 0
            for v in graph[u]:
                av = a[v]
                total += (1 - av) * modinv(av)
            R[u] = total % MOD

        # Compute T_arr[u] = (1 - a[u]) * P[u] * R[u]
        T_arr = [0] * (n + 1)
        for u in range(1, n + 1):
            T_arr[u] = ((1 - a[u]) % MOD) * P[u] % MOD * R[u] % MOD

        Y = 0
        for u in range(1, n + 1):
            Y += T_arr[u]
        Y %= MOD

        sumTsq = 0
        for u in range(1, n + 1):
            sumTsq += T_arr[u] * T_arr[u]
        sumTsq %= MOD

        total_sq = (Y * Y - sumTsq) % MOD
        part1 = total_sq * inv2 % MOD

        # S_adj = sum over edges (u,v) of (1 - a[u])*(1 - a[v])*P[u]*P[v]*inv(a[u])*inv(a[v])
        S_adj = 0
        inv_a = [0] * (n + 1)
        for i in range(1, n + 1):
            inv_a[i] = modinv(a[i])
        for u, v in edges:
            term_edge = (1 - a[u]) * (1 - a[v]) % MOD
            term_edge = term_edge * P[u] % MOD
            term_edge = term_edge * P[v] % MOD
            term_edge = term_edge * inv_a[u] % MOD
            term_edge = term_edge * inv_a[v] % MOD
            S_adj = (S_adj + term_edge) % MOD

        # S_adj_T = sum over edges (u,v) of T_arr[u]*T_arr[v]
        S_adj_T = 0
        for u, v in edges:
            S_adj_T = (S_adj_T + T_arr[u] * T_arr[v]) % MOD

        # S_common_T and S_common_corrected
        S_common_T = 0
        S_common_corrected = 0
        for w in range(1, n + 1):
            neighbors = graph[w]
            deg = len(neighbors)
            if deg == 0:
                continue
            c = (1 - a[w]) * inv_a[w] % MOD

            A_val = 0
            S1_val = 0
            B_val = 0
            S2_val = 0
            X_val = 0
            sq_T_val = 0

            # Precompute R[u] - c for neighbors u
            for u in neighbors:
                f_u = (1 - a[u]) * P[u] % MOD
                A_val = (A_val + f_u) % MOD
                S1_val = (S1_val + f_u * f_u) % MOD
            for u in neighbors:
                f_u = (1 - a[u]) * P[u] % MOD
                g_u = f_u * ((R[u] - c) % MOD) % MOD
                B_val = (B_val + g_u) % MOD
                S2_val = (S2_val + g_u * g_u) % MOD
            for u in neighbors:
                X_val = (X_val + T_arr[u]) % MOD
                sq_T_val = (sq_T_val + T_arr[u] * T_arr[u]) % MOD

            term1 = (1 - a[w]) * ((A_val * A_val - S1_val) % MOD) % MOD
            term2 = a[w] * ((B_val * B_val - S2_val) % MOD) % MOD
            numerator = (term1 + term2) % MOD

            term_w = numerator * inv2 % MOD
            term_w = term_w * inv_a[w] % MOD
            term_w = term_w * inv_a[w] % MOD
            S_common_corrected = (S_common_corrected + term_w) % MOD

            common_T_w = (X_val * X_val - sq_T_val) % MOD
            common_T_w = common_T_w * inv2 % MOD
            S_common_T = (S_common_T + common_T_w) % MOD

        ans = (S_adj + part1 - S_adj_T - S_common_T + S_common_corrected) % MOD
        results.append(str(ans))

    print("\n".join(results))


if __name__ == "__main__":
    main()