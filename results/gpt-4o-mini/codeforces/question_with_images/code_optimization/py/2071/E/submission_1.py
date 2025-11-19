import sys
MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        p = [0] * (n + 1)
        q = [0] * (n + 1)
        a = [0] * (n + 1)
        
        for i in range(1, n + 1):
            p[i] = int(data[idx])
            q[i] = int(data[idx + 1])
            a[i] = p[i] * pow(q[i], MOD - 2, MOD) % MOD
            idx += 2
        
        graph = [[] for _ in range(n + 1)]
        edges = []
        
        for __ in range(n - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            graph[u].append(v)
            graph[v].append(u)
            edges.append((u, v))
            idx += 2

        P = [1] * (n + 1)
        R = [0] * (n + 1)

        for u in range(1, n + 1):
            total = 0
            prod = 1
            for v in graph[u]:
                prod = prod * a[v] % MOD
                total = (total + (1 - a[v]) * pow(a[v], MOD - 2, MOD)) % MOD
            
            P[u] = prod
            R[u] = total

        T_arr = [0] * (n + 1)
        for u in range(1, n + 1):
            T_arr[u] = ( (1 - a[u]) * P[u] % MOD * R[u] ) % MOD

        Y = sum(T_arr) % MOD
        
        sumTsq = sum((T_arr[i] * T_arr[i]) % MOD for i in range(1, n + 1)) % MOD
        total_sq = (Y * Y - sumTsq) % MOD
        if total_sq < 0:
            total_sq += MOD
        part1 = total_sq * pow(2, MOD - 2, MOD) % MOD
        
        S_adj = sum(( (1 - a[u]) * (1 - a[v]) % MOD * P[u] % MOD * P[v] % MOD * 
                       pow(a[u], MOD - 2, MOD) % MOD * pow(a[v], MOD - 2, MOD) % MOD) 
                      for (u, v) in edges) % MOD
        
        S_adj_T = sum((T_arr[u] * T_arr[v]) % MOD for (u, v) in edges) % MOD

        S_common_T = 0
        S_common_corrected = 0
        
        for w in range(1, n + 1):
            neighbors = graph[w]
            if not neighbors:
                continue
            
            c = (1 - a[w]) * pow(a[w], MOD - 2, MOD) % MOD
            A_val = S1_val = B_val = S2_val = X_val = sq_T_val = 0
            
            for u in neighbors:
                f_u = (1 - a[u]) * P[u] % MOD
                A_val = (A_val + f_u) % MOD
                S1_val = (S1_val + f_u * f_u) % MOD
                g_u = f_u * ((R[u] - c) % MOD) % MOD
                B_val = (B_val + g_u) % MOD
                S2_val = (S2_val + g_u * g_u) % MOD
                X_val = (X_val + T_arr[u]) % MOD
                sq_T_val = (sq_T_val + T_arr[u] * T_arr[u]) % MOD
            
            term1 = (1 - a[w]) * ((A_val * A_val - S1_val) % MOD) % MOD
            term2 = a[w] * ((B_val * B_val - S2_val) % MOD) % MOD
            numerator = (term1 + term2) % MOD
            term_w = numerator * pow(2, MOD - 2, MOD) % MOD * pow(a[w], MOD - 2, MOD) % MOD * pow(a[w], MOD - 2, MOD) % MOD
            
            S_common_corrected = (S_common_corrected + term_w) % MOD
            
            common_T_w = (X_val * X_val - sq_T_val) % MOD
            if common_T_w < 0:
                common_T_w += MOD
            common_T_w = common_T_w * pow(2, MOD - 2, MOD) % MOD
            
            S_common_T = (S_common_T + common_T_w) % MOD

        ans = (S_adj + part1 - S_adj_T - S_common_T + S_common_corrected) % MOD
        if ans < 0:
            ans += MOD
        results.append(str(ans))

    print("\n".join(results))

if __name__ == "__main__":
    main()