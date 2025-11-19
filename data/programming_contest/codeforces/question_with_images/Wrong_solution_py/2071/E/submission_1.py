import sys

MOD = 998244353
INV2 = (MOD + 1) // 2


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        r = [0] * (n + 1)
        s = [0] * (n + 1)
        inv_r = [0] * (n + 1)
        s_inv_r = [0] * (n + 1)

        for i in range(1, n + 1):
            p = next(it)
            q = next(it)
            inv_q = pow(q, MOD - 2, MOD)
            ri = p * inv_q % MOD
            r[i] = ri
            s[i] = (1 - ri) % MOD
            inv_ri = pow(ri, MOD - 2, MOD)
            inv_r[i] = inv_ri
            s_inv_r[i] = s[i] * inv_ri % MOD

        g = [[] for _ in range(n + 1)]
        edges = []
        R = [1] * (n + 1)
        total_sum = [0] * (n + 1)

        for _ in range(n - 1):
            u = next(it)
            v = next(it)
            g[u].append(v)
            g[v].append(u)
            edges.append((u, v))

            R[u] = R[u] * r[v] % MOD
            R[v] = R[v] * r[u] % MOD

            total_sum[u] = (total_sum[u] + s_inv_r[v]) % MOD
            total_sum[v] = (total_sum[v] + s_inv_r[u]) % MOD


        leaf = [0] * (n + 1)
        a = [0] * (n + 1)

        for i in range(1, n + 1):
            leaf[i] = s[i] * R[i] % MOD * total_sum[i] % MOD
            a[i] = s[i] * R[i] % MOD

        S = sum(leaf[1:]) % MOD
        S2 = sum((x * x) % MOD for x in leaf[1:]) % MOD
        independent = (S * S - S2) % MOD
        independent = independent * INV2 % MOD

        corrections = 0

        for u, v in edges:
            real = s[u] * s[v] % MOD
            real = real * R[u] % MOD
            real = real * R[v] % MOD
            real = real * inv_r[u] % MOD
            real = real * inv_r[v] % MOD

            prod = leaf[u] * leaf[v] % MOD
            corrections = (corrections + real - prod) % MOD 


        for k in range(1, n + 1):
            neigh = g[k]
            if len(neigh) < 2:
                continue

            Ak = 0
            A2k = 0
            Ck = 0
            C2k = 0
            Dk = 0
            D2k = 0
            sk_inv_rk = s_inv_r[k]

            for v in neigh:
                av = a[v]
                bv = (total_sum[v] - sk_inv_rk) % MOD 
                cv = av * bv % MOD
                lv = leaf[v]

                Ak = (Ak + av) % MOD
                A2k = (A2k + av * av) % MOD
                Ck = (Ck + cv) % MOD
                C2k = (C2k + cv * cv) % MOD
                Dk = (Dk + lv) % MOD
                D2k = (D2k + lv * lv) % MOD
            alpha = s[k] * inv_r[k] % MOD * inv_r[k] % MOD

            part1 = (Ak * Ak - A2k) % MOD
            part1 = part1 * INV2 % MOD
            part1 = part1 * alpha % MOD

            part2 = (Ck * Ck - C2k) % MOD
            part2 = part2 * INV2 % MOD

            real_k = (part1 + part2) % MOD

            indep_k = (Dk * Dk - D2k) % MOD
            indep_k = indep_k * INV2 % MOD

            corrections = (corrections + real_k - indep_k) % MOD

        answer = (independent + corrections) % MOD
        out.append(str(answer))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
