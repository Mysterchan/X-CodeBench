import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# 预处理3的幂
max_n = 3000
pow3 = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    pow3[i] = pow3[i-1] * 3 % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    edges = [[] for __ in range(n)]
    for __ in range(n-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    # 计算所有点对距离
    # 由于n最大3000，O(n^2) BFS可行
    dist = [[-1]*n for __ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        queue = [i]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for w in edges[u]:
                if dist[i][w] == -1:
                    dist[i][w] = dist[i][u] + 1
                    queue.append(w)

    # 题意：
    # 对所有3^n种着色，计算酷炫度总和
    # 酷炫度 = max dist(u,v) 其中 c_u=红, c_v=蓝
    # 若无红或无蓝，酷炫度=0

    # 观察：
    # 对每个距离d，计算有多少着色的酷炫度 >= d
    # 设f(d) = 有酷炫度 >= d的着色数
    # 则答案 = sum_{d=1}^{diameter} (f(d) - f(d+1)) * d
    # = sum_{d=1}^{diameter} f(d)

    # 计算f(d):
    # 酷炫度 >= d 意味着存在红点u和蓝点v，dist(u,v) >= d
    # 等价于存在一对点(u,v)距离>=d，且u红,v蓝
    # 反过来，酷炫度 < d 意味着所有红蓝点对距离 < d

    # 计算g(d) = 酷炫度 < d的着色数
    # g(d) = 3^n - f(d)

    # 酷炫度 < d 意味着不存在红蓝点对距离 >= d
    # 即任意距离 >= d的点对中，不能同时有红和蓝
    # 也就是说，所有距离 >= d的点对，要么都不是红蓝组合

    # 这等价于构造一个图G_d，点为树的顶点，
    # 边连接所有距离 >= d的点对
    # 在G_d中，红色和蓝色的点不能在同一个连通分量中同时出现
    # 因为连通分量内任意两点距离 >= d（通过边定义）
    # 所以每个连通分量内的点只能是：
    # - 全白
    # - 全红
    # - 全蓝
    # 不能混红蓝

    # 对每个连通分量大小为sz，有3种颜色选择：
    # - 全白：1种
    # - 全红：1种
    # - 全蓝：1种
    # 总共3种选择

    # 因此，g(d) = ∏_{连通分量} 3 = 3^{连通分量数}

    # 计算连通分量数：
    # G_d的边是所有距离 >= d的点对
    # 计算G_d的连通分量数 = n - 边数 + 环数
    # 但环数不好直接算，改用并查集

    # 由于d从1到最大距离，边集递减（距离>=d的边数递减）
    # 我们从d=1开始，G_1是完全图（所有距离>=1的边都在）
    # 随着d增大，边减少，连通分量数增加

    # 预处理所有边按距离排序
    # 对d从最大距离到1倒序处理，维护并查集
    # 这样可以快速得到每个d的连通分量数

    # 先统计所有边的距离
    edges_dist = []
    max_dist = 0
    for i in range(n):
        for j in range(i+1,n):
            d = dist[i][j]
            edges_dist.append((d,i,j))
            if d > max_dist:
                max_dist = d

    edges_dist.sort(reverse=True)  # 按距离降序

    # 并查集
    parent = list(range(n))
    size = [1]*n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        a=find(a)
        b=find(b)
        if a==b:
            return False
        if size[a]<size[b]:
            a,b=b,a
        parent[b]=a
        size[a]+=size[b]
        return True

    # 初始化
    # d从max_dist+1开始，G_d无边，连通分量数=n
    # 我们从d=max_dist+1到1倒序加入边（距离>=d的边）
    # 维护连通分量数
    cc = n
    res_g = [0]*(max_dist+2)  # g(d) for d in [1..max_dist+1], g(max_dist+1)=3^n (no edges)
    res_g[max_dist+1] = pow3[n]

    idx = 0
    for d in range(max_dist,0,-1):
        # 加入所有距离==d的边
        while idx < len(edges_dist) and edges_dist[idx][0] == d:
            _,u,v = edges_dist[idx]
            if union(u,v):
                cc -= 1
            idx += 1
        # g(d) = 3^{cc}
        res_g[d] = pow3[cc]

    # f(d) = 3^n - g(d)
    # 答案 = sum_{d=1}^{max_dist} f(d) = sum (3^n - g(d)) = max_dist*3^n - sum g(d)
    ans = (max_dist * pow3[n]) % MOD
    ans -= sum(res_g[1:max_dist+1])
    ans %= MOD

    print(ans)