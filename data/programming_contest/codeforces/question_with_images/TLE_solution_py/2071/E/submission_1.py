import sys
MOD = 998244353

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        p_list = [0] * (n+1)
        q_list = [0] * (n+1)
        for i in range(1, n+1):
            pi = int(data[index]); qi = int(data[index+1]); index += 2
            p_list[i] = pi
            q_list[i] = qi

        a = [0] * (n+1)
        for i in range(1, n+1):
            a[i] = p_list[i] * pow(q_list[i], MOD-2, MOD) % MOD

        graph = [[] for _ in range(n+1)]
        edges = []
        for i in range(n-1):
            u = int(data[index]); v = int(data[index+1]); index += 2
            graph[u].append(v)
            graph[v].append(u)
            if u < v:
                edges.append((u, v))
            else:
                edges.append((v, u))

        P = [0] * (n+1)
        R = [0] * (n+1)
        for u in range(1, n+1):
            prod = 1
            total = 0
            for v in graph[u]:
                prod = prod * a[v] % MOD
                total = (total + (1 - a[v]) * pow(a[v], MOD-2, MOD)) % MOD
            P[u] = prod
            R[u] = total

        T_arr = [0] * (n+1)
        for u in range(1, n+1):
            T_arr[u] = ( (1 - a[u]) % MOD * P[u] % MOD * R[u] ) % MOD

        Y = 0
        for i in range(1, n+1):
            Y = (Y + T_arr[i]) % MOD

        sumTsq = 0
        for i in range(1, n+1):
            sumTsq = (sumTsq + T_arr[i]*T_arr[i]) % MOD
        total_sq = (Y*Y - sumTsq) % MOD
        if total_sq < 0:
            total_sq += MOD
        part1 = total_sq * pow(2, MOD-2, MOD) % MOD

        S_adj = 0
        for (u, v) in edges:
            term_edge = (1 - a[u]) * (1 - a[v]) % MOD
            term_edge = term_edge * P[u] % MOD
            term_edge = term_edge * P[v] % MOD
            term_edge = term_edge * pow(a[u], MOD-2, MOD) % MOD
            term_edge = term_edge * pow(a[v], MOD-2, MOD) % MOD
            S_adj = (S_adj + term_edge) % MOD

        S_adj_T = 0
        for (u, v) in edges:
            S_adj_T = (S_adj_T + T_arr[u] * T_arr[v]) % MOD

        S_common_T = 0
        S_common_corrected = 0
        for w in range(1, n+1):
            neighbors = graph[w]
            if not neighbors:
                continue
            c = (1 - a[w]) * pow(a[w], MOD-2, MOD) % MOD
            A_val = 0
            S1_val = 0
            B_val = 0
            S2_val = 0
            X_val = 0
            sq_T_val = 0
            for u in neighbors:
                f_u = (1 - a[u]) * P[u] % MOD
                A_val = (A_val + f_u) % MOD
                S1_val = (S1_val + f_u * f_u) % MOD
                g_u = f_u * ( (R[u] - c) % MOD ) % MOD
                B_val = (B_val + g_u) % MOD
                S2_val = (S2_val + g_u * g_u) % MOD
                X_val = (X_val + T_arr[u]) % MOD
                sq_T_val = (sq_T_val + T_arr[u] * T_arr[u]) % MOD

            term1 = (1 - a[w]) * ( (A_val*A_val - S1_val) % MOD ) % MOD
            term2 = a[w] * ( (B_val*B_val - S2_val) % MOD ) % MOD
            numerator = (term1 + term2) % MOD
            term_w = numerator * pow(2, MOD-2, MOD) % MOD
            term_w = term_w * pow(a[w], MOD-2, MOD) % MOD
            term_w = term_w * pow(a[w], MOD-2, MOD) % MOD
            S_common_corrected = (S_common_corrected + term_w) % MOD

            common_T_w = (X_val * X_val - sq_T_val) % MOD
            if common_T_w < 0:
                common_T_w += MOD
            common_T_w = common_T_w * pow(2, MOD-2, MOD) % MOD
            S_common_T = (S_common_T + common_T_w) % MOD

        ans = (S_adj + part1 - S_adj_T - S_common_T + S_common_corrected) % MOD
        if ans < 0:
            ans += MOD
        results.append(str(ans))

    print("\n".join(results))

if __name__ == "__main__":
    main()
