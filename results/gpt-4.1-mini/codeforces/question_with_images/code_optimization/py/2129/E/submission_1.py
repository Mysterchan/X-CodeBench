import sys
import math
import threading
def main():
    input = sys.stdin.readline
    t = int(input())
    out_lines = []
    MAX_VAL = (1 << 18)
    bucket_size = 512
    num_buckets = (MAX_VAL + bucket_size - 1) // bucket_size

    for _ in range(t):
        while True:
            line = input()
            if line.strip():
                n, m = map(int, line.split())
                break
        adj = [[] for __ in range(n + 1)]
        for __ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        q = int(input())
        queries = []
        for i in range(q):
            l, r, k = map(int, input().split())
            queries.append((l, r, k, i))

        if n == 0:
            out_lines.extend(['0'] * q)
            continue

        block_size = int(n ** 0.5) + 1
        queries.sort(key=lambda x: (x[0] // block_size, x[1]))

        active = [False] * (n + 1)
        B = [0] * (n + 1)
        freq = [0] * (MAX_VAL + 1)
        buckets = [0] * num_buckets

        def update_freq(val, delta):
            # val always in [0, MAX_VAL]
            freq[val] += delta
            b_idx = val // bucket_size
            buckets[b_idx] += delta

        def kth_smallest(k):
            # Find k-th smallest value in freq using buckets
            for i in range(num_buckets):
                if k <= buckets[i]:
                    start = i * bucket_size
                    end = min(MAX_VAL + 1, (i + 1) * bucket_size)
                    for j in range(start, end):
                        if k <= freq[j]:
                            return j
                        k -= freq[j]
                    # Should never reach here if freq sums are correct
                    return -1
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

        mo_l, mo_r = 1, 0
        ans = [0] * q

        for l, r, k, idx in queries:
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
            ans[idx] = kth_smallest(k)

        out_lines.extend(map(str, ans))

    print('\n'.join(out_lines))


if __name__ == "__main__":
    threading.Thread(target=main,).start()