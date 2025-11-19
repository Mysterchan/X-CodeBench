import sys
import math

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out_lines = []
    for _ in range(t):
        data = input().split()
        if not data:
            continue
        n = int(data[0])
        m = int(data[1])
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        q = int(input().strip())
        queries = []
        for i in range(q):
            l, r, k = map(int, input().split())
            queries.append((l, r, k, i))

        if n == 0:
            for _ in range(q):
                out_lines.append("0")
            continue

        block_size = int(math.sqrt(n)) + 1
        queries.sort(key=lambda x: (x[0] // block_size, x[1]))

        active = [False] * (n+1)
        B = [0] * (n+1)
        M = 1 << 18
        freq = [0] * (M+1)
        bucket_size = 512
        num_buckets = (M + bucket_size - 1) // bucket_size
        buckets = [0] * num_buckets

        def update_freq(val, delta):
            if val < 0 or val > M:
                return
            freq[val] += delta
            b_idx = val // bucket_size
            if b_idx < num_buckets:
                buckets[b_idx] += delta

        def kth_smallest(k):
            for i in range(num_buckets):
                if k <= buckets[i]:
                    start = i * bucket_size
                    end = min(M+1, (i+1)*bucket_size)
                    for j in range(start, end):
                        if k <= freq[j]:
                            return j
                        k -= freq[j]
                else:
                    k -= buckets[i]
            return -1

        def activate(x):
            active[x] = True
            B[x] = 0
            for u in adj[x]:
                if active[u]:
                    update_freq(B[u], -1)
                    B[u] ^= x
                    update_freq(B[u], 1)
                    B[x] ^= u
            update_freq(B[x], 1)

        def deactivate(x):
            update_freq(B[x], -1)
            for u in adj[x]:
                if active[u]:
                    update_freq(B[u], -1)
                    B[u] ^= x
                    update_freq(B[u], 1)
            active[x] = False

        mo_l = 1
        mo_r = 0
        ans = [-1] * q

        for query in queries:
            l, r, k, idx = query
            while mo_r < r:
                mo_r += 1
                activate(mo_r)
            while mo_r > r:
                deactivate(mo_r)
                mo_r -= 1
            while mo_l < l:
                deactivate(mo_l)
                mo_l += 1
            while mo_l > l:
                mo_l -= 1
                activate(mo_l)
            res = kth_smallest(k)
            ans[idx] = res

        for i in range(q):
            out_lines.append(str(ans[i]))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
