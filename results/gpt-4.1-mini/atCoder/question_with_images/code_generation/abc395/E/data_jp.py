import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    # グラフの辺を2つ用意（反転状態0と1）
    # state=0: 辺は元の向き
    # state=1: 辺は反転した向き
    # 各状態での隣接リストを作成
    # state=0のときはu->vの辺
    # state=1のときはv->uの辺（反転）
    g = [[] for _ in range(N+1)]
    gr = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        g[u].append(v)
        gr[v].append(u)

    # dist[node][state] : 頂点nodeにstate状態で到達する最小コスト
    INF = 1 << 60
    dist = [[INF]*2 for _ in range(N+1)]
    dist[1][0] = 0

    # 優先度付きキュー (cost, node, state)
    hq = [(0, 1, 0)]
    while hq:
        cost, v, state = heapq.heappop(hq)
        if dist[v][state] < cost:
            continue
        if v == N:
            print(cost)
            return
        # 1. 辺をたどる（コスト1）
        if state == 0:
            for nv in g[v]:
                ncost = cost + 1
                if dist[nv][state] > ncost:
                    dist[nv][state] = ncost
                    heapq.heappush(hq, (ncost, nv, state))
        else:
            for nv in gr[v]:
                ncost = cost + 1
                if dist[nv][state] > ncost:
                    dist[nv][state] = ncost
                    heapq.heappush(hq, (ncost, nv, state))
        # 2. 辺の向きを反転する（コストX）
        nstate = 1 - state
        ncost = cost + X
        if dist[v][nstate] > ncost:
            dist[v][nstate] = ncost
            heapq.heappush(hq, (ncost, v, nstate))

if __name__ == "__main__":
    main()