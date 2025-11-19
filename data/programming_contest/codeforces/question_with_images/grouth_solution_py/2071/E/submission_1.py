MOD = 998244353

import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        p_list = [0] * (n+1)
        for i in range(1, n+1):
            p = int(data[index]); q = int(data[index+1]); index += 2
            inv_q = pow(q, MOD-2, MOD)
            s_i = (1 - p * inv_q) % MOD
            p_list[i] = s_i

        graph = [[] for _ in range(n+1)]
        for i in range(n-1):
            u = int(data[index]); v = int(data[index+1]); index += 2
            graph[u].append(v)
            graph[v].append(u)

        T = [1] * (n+1)
        d = [0] * (n+1)
        a = [0] * (n+1)

        for u in range(1, n+1):
            for v in graph[u]:
                T[u] = (T[u] * (1 - p_list[v])) % MOD
                d[u] = (d[u] + p_list[v] * pow(1 - p_list[v], MOD-2, MOD)) % MOD

        for u in range(1, n+1):
            a[u] = p_list[u] * T[u] % MOD * d[u] % MOD

        S = 0
        sq_sum = 0
        for i in range(1, n+1):
            S = (S + a[i]) % MOD
            sq_sum = (sq_sum + a[i] * a[i]) % MOD

        inv2 = pow(2, MOD-2, MOD)
        independent_sum = (S * S - sq_sum) % MOD * inv2 % MOD
        correction = 0

        for u in range(1, n+1):
            for v in graph[u]:
                if u < v:
                    term = p_list[u] * p_list[v] % MOD * T[u] % MOD * T[v] % MOD
                    denom = (1 - p_list[u]) * (1 - p_list[v]) % MOD
                    term = term * pow(denom, MOD-2, MOD) % MOD
                    indep = a[u] * a[v] % MOD
                    correction = (correction + term - indep) % MOD

        for w in range(1, n+1):
            neighbors = graph[w]
            if len(neighbors) < 2:
                continue
            total_A = 0
            total_A2 = 0
            total_a = 0
            total_a2 = 0
            total_S2 = 0
            total_S4 = 0
            for u in neighbors:
                A_u = p_list[u] * T[u] % MOD
                d_u_prime = (d[u] - p_list[w] * pow(1 - p_list[w], MOD-2, MOD)) % MOD
                total_A = (total_A + A_u) % MOD
                total_A2 = (total_A2 + A_u * A_u) % MOD
                total_a = (total_a + a[u]) % MOD
                total_a2 = (total_a2 + a[u] * a[u]) % MOD
                temp = A_u * d_u_prime % MOD
                total_S2 = (total_S2 + temp) % MOD
                total_S4 = (total_S4 + temp * temp) % MOD

            term1 = (total_A * total_A - total_A2) % MOD
            term1 = term1 * inv2 % MOD
            term2 = (total_S2 * total_S2 - total_S4) % MOD
            term2 = term2 * inv2 % MOD
            total_term = (p_list[w] * term1 + (1 - p_list[w]) * term2) % MOD
            denom2 = pow((1 - p_list[w]) * (1 - p_list[w]) % MOD, MOD-2, MOD)
            total_term = total_term * denom2 % MOD
            independent_part = (total_a * total_a - total_a2) % MOD * inv2 % MOD
            correction = (correction + total_term - independent_part) % MOD

        ans = (independent_sum + correction) % MOD
        if ans < 0:
            ans += MOD
        results.append(str(ans))

    print("\n".join(results))

if __name__ == "__main__":
    main()
