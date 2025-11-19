import sys
import math
import bisect

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    max_val = 1 << 18

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

        sorted_adj = [None] * (n+1)
        prefix_xor = [None] * (n+1)
        for i in range(1, n+1):
            lst = sorted(adj[i])
            sorted_adj[i] = lst
            px = [0]
            for num in lst:
                px.append(px[-1] ^ num)
            prefix_xor[i] = px

        fenw = [0] * (max_val + 2)

        def fenw_update(i, delta):
            idx = i + 1
            while idx <= max_val + 1:
                fenw[idx] += delta
                idx += idx & -idx

        def fenw_prefix(i):
            if i < 0:
                return 0
            res = 0
            idx = i + 1
            while idx:
                res += fenw[idx]
                idx -= idx & -idx
            return res

        def kth_element(k):
            low, high = 0, max_val
            ans = high
            while low <= high:
                mid = (low + high) // 2
                if fenw_prefix(mid) >= k:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        q = int(input().strip())
        queries = []
        for i in range(q):
            l, r, k = map(int, input().split())
            queries.append((l, r, k, i))

        block_size = int(math.sqrt(n))
        queries.sort(key=lambda x: (x[0] // block_size, x[1]))

        cur_val = [0] * (n + 1)
        L = 1
        R = 0
        ans_arr = [0] * q

        def add_node(x):
            nonlocal L, R
            lst = sorted_adj[x]
            px = prefix_xor[x]
            idx1 = bisect.bisect_right(lst, x)
            value1 = px[idx1]
            idx2 = bisect.bisect_right(lst, L - 1)
            value2 = px[idx2]
            value_x = value1 ^ value2
            fenw_update(value_x, 1)
            cur_val[x] = value_x
            for u in lst:
                if u < L or u > x:
                    continue
                old_val = cur_val[u]
                new_val = old_val ^ x
                fenw_update(old_val, -1)
                fenw_update(new_val, 1)
                cur_val[u] = new_val

        def remove_node(x):
            nonlocal L, R
            val = cur_val[x]
            fenw_update(val, -1)
            lst = sorted_adj[x]
            for u in lst:
                if u < x + 1 or u > R:
                    continue
                old_val = cur_val[u]
                new_val = old_val ^ x
                fenw_update(old_val, -1)
                fenw_update(new_val, 1)
                cur_val[u] = new_val

        for ql, qr, k, idx in queries:
            while R < qr:
                R += 1
                add_node(R)
            while R > qr:
                remove_node(R)
                R -= 1
            while L < ql:
                remove_node(L)
                L += 1
            while L > ql:
                L -= 1
                add_node(L)
            ans_arr[idx] = kth_element(k)

        for ans in ans_arr:
            print(ans)

if __name__ == "__main__":
    main()
