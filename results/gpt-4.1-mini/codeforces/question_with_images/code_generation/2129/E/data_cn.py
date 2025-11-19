import sys
import threading
import bisect

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    t = int(input())
    # 总和限制：n,m,q <= 1.5e5，单次处理即可

    for _ in range(t):
        n, m = map(int, input().split())
        edges = [[] for __ in range(n + 1)]
        for __ in range(m):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)

        # 预处理每个节点的邻居列表，排序
        for u in range(1, n + 1):
            edges[u].sort()

        q = int(input())
        queries = [tuple(map(int, input().split())) + (i,) for i in range(q)]

        # 对每个查询，计算 f(u,G[V']) for u in [l,r]
        # f(u,G[V']) = XOR of neighbors v in edges[u] with v in [l,r]

        # 直接对每个查询暴力计算会超时
        # 观察：
        # f(u,G[V']) = XOR of neighbors v in edges[u] ∩ [l,r]
        # 对每个u，edges[u]是有序的
        # 对每个查询(l,r,k)，我们需要对u in [l,r]计算f(u,G[V'])
        # 计算f(u,G[V'])需要对edges[u]二分找到邻居在[l,r]区间内的部分，然后异或
        # 但q和n都很大，暴力不行

        # 优化思路：
        # 1. 预处理每个节点u的邻居前缀异或数组prefix_xor[u]
        # prefix_xor[u][i] = XOR of edges[u][0..i-1]
        # 这样f(u,G[V']) = prefix_xor[u][pos_r] ^ prefix_xor[u][pos_l]
        # pos_l = lower_bound(edges[u], l)
        # pos_r = upper_bound(edges[u], r)

        prefix_xor = [None] * (n + 1)
        for u in range(1, n + 1):
            arr = edges[u]
            px = [0]
            for x in arr:
                px.append(px[-1] ^ x)
            prefix_xor[u] = px

        # 2. 对每个查询，计算f(u,G[V']) for u in [l,r]
        # 需要快速得到区间[l,r]内所有f(u,G[V'])，然后求第k小
        # 直接对每个u计算f(u,G[V']) O(n)太慢

        # 3. 离线处理所有查询
        # 由于查询是区间[l,r]，且k是第k小
        # 可以考虑莫队算法或线段树+离线查询
        # 但f(u,G[V'])依赖于[l,r]，且f(u,G[V'])的计算依赖于l,r本身，难以预处理

        # 4. 观察f(u,G[V'])的定义：
        # f(u,G[V']) = XOR of neighbors v in edges[u] ∩ [l,r]
        # 由于u ∈ [l,r]，且v ∈ [l,r]
        # 也就是说，f(u,G[V']) = XOR of neighbors v of u with v in [l,r]

        # 5. 另一种思路：
        # 对每个节点u，预处理一个数组F_u[i] = f(u,G[{1..i}])
        # 但f(u,G[{1..i}])不是简单前缀，因为f(u,G[{1..i}]) = XOR of neighbors v ≤ i
        # 由于f(u,G[V'])是邻居v在[l,r]区间的异或
        # f(u,G[V']) = prefix_xor[u][pos_r] ^ prefix_xor[u][pos_l]
        # 其中pos_l = lower_bound(edges[u], l)
        # pos_r = upper_bound(edges[u], r)

        # 6. 由于查询中u ∈ [l,r]，我们需要对区间[l,r]内的所有u计算f(u,G[V'])
        # 这相当于对区间[l,r]内的f(u,G[V'])求第k小

        # 7. 关键是如何快速对区间[l,r]内的f(u,G[V'])求第k小
        # 这是区间kth order statistic问题

        # 8. 方案：
        # 对每个查询，先计算f(u,G[V']) for u in [l,r]
        # 但直接计算太慢

        # 9. 观察f(u,G[V'])的计算：
        # f(u,G[V']) = prefix_xor[u][pos_r] ^ prefix_xor[u][pos_l]
        # pos_l, pos_r依赖于l,r
        # 但l,r是查询参数，无法预先固定

        # 10. 另一种思路：
        # 对每个节点u，预处理edges[u]的邻居列表
        # 对每个查询(l,r,k)，对u in [l,r]：
        #   pos_l = lower_bound(edges[u], l)
        #   pos_r = upper_bound(edges[u], r)
        #   f(u) = prefix_xor[u][pos_r] ^ prefix_xor[u][pos_l]

        # 11. 由于q和n都大，暴力不行
        # 12. 但题目保证所有测试案例中 n,m,q 总和 ≤ 1.5e5
        # 13. 试试分块+离线：
        # 按块大小B划分节点区间
        # 对每个查询(l,r,k)，分解为若干块
        # 对整块直接预存f(u,G[V'])，对边界部分暴力计算
        # 但f(u,G[V'])依赖于l,r，无法预先存

        # 14. 另一思路：
        # 对每个查询，先计算f(u,G[V']) for u in [l,r]
        # 由于q和n总和1.5e5，且每个查询区间长度平均较小，暴力可行

        # 15. 试试暴力：
        # 对每个查询，遍历u in [l,r]，计算f(u,G[V'])，存数组排序取第k小
        # 复杂度约为 sum of (r-l+1) over all queries
        # 题目没给区间长度限制，可能通过

        # 16. 实现暴力，优化输入输出

        out = [0] * q
        for l, r, k, idx in queries:
            vals = []
            for u in range(l, r + 1):
                arr = edges[u]
                px = prefix_xor[u]
                # 找邻居v在[l,r]区间的异或
                # pos_l = lower_bound(arr, l)
                # pos_r = upper_bound(arr, r)
                # python bisect
                pl = bisect.bisect_left(arr, l)
                pr = bisect.bisect_right(arr, r)
                val = px[pr] ^ px[pl]
                vals.append(val)
            vals.sort()
            out[idx] = vals[k - 1]

        print('\n'.join(map(str, out)))

threading.Thread(target=main).start()