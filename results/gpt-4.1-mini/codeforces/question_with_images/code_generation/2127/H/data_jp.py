import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for __ in range(m)]

        # 頂点の次数制限は最大2なので、最大マッチングのように考えられるが、
        # ここでは「次数が最大2」の制約の下で最大の辺集合を選ぶ問題。
        # これは「最大次数制約付き部分グラフの最大辺数問題」であり、
        # 制約が小さいので、最大マッチングの拡張として「次数制約付き最大マッチング」を
        # 解くことができる。
        #
        # 具体的には、次数制約2のため、各頂点は最大2本の辺を選べる。
        # これをフロー問題に変換する。
        #
        # フローグラフ構築:
        # - ソースSから各辺に容量1の辺を張る（辺を選ぶか選ばないか）
        # - 各辺からその両端の頂点に容量1の辺を張る
        # - 各頂点からシンクTに容量2の辺を張る（頂点の次数制限）
        #
        # このフローの最大値が、次数制限2の下で選べる最大の辺数となる。

        S = 0
        T = 1 + m + n  # ソース0, 辺は1~m, 頂点はm+1~m+n, シンクはT
        size = T + 1

        graph = [[] for __ in range(size)]

        def add_edge(u, v, cap):
            graph[u].append([v, cap, len(graph[v])])
            graph[v].append([u, 0, len(graph[u]) - 1])

        # ソース -> 辺ノード
        for i in range(m):
            add_edge(S, i+1, 1)

        # 辺ノード -> 頂点ノード
        for i, (u, v) in enumerate(edges):
            u_node = m + u
            v_node = m + v
            add_edge(i+1, u_node, 1)
            add_edge(i+1, v_node, 1)

        # 頂点ノード -> シンク
        for i in range(1, n+1):
            add_edge(m + i, T, 2)

        # Dinic法で最大流を求める
        flow = 0
        INF = 10**9

        while True:
            level = [-1]*size
            level[S] = 0
            queue = [S]
            for u in queue:
                for i, (v, cap, rev) in enumerate(graph[u]):
                    if cap > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[T] < 0:
                break

            iter = [0]*size

            def dfs(u, f):
                if u == T:
                    return f
                while iter[u] < len(graph[u]):
                    v, cap, rev = graph[u][iter[u]]
                    if cap > 0 and level[u] < level[v]:
                        d = dfs(v, min(f, cap))
                        if d > 0:
                            graph[u][iter[u]][1] -= d
                            graph[v][rev][1] += d
                            return d
                    iter[u] += 1
                return 0

            while True:
                f = dfs(S, INF)
                if f == 0:
                    break
                flow += f

        print(flow)

if __name__ == "__main__":
    main()