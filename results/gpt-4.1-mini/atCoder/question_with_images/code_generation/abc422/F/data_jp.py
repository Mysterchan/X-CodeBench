import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    # dist[i]: 高橋くんが頂点iに到達するまでに消費する燃料の最小値
    dist = [float('inf')] * N
    dist[0] = 0  # 頂点1にいるときの燃料消費は0

    # 優先度付きキュー (燃料消費, 頂点, 現在の体重)
    # 体重は頂点に到達した時点で増加しているので、distに記録されている燃料消費と体重は対応する
    # ここでは体重はdist + W[i]の累積で管理する必要があるが、distは燃料消費なので、
    # 体重は頂点に到達した時点での累積体重 = 頂点1のW[0] + それ以降のWの和
    # しかし、distは燃料消費であり、体重はdist + W[i]の累積ではない。
    # 体重は頂点に到達した時点での累積Wの和。
    # そこで、dist[i]は燃料消費の最小値、weight[i]は頂点iに到達した時点の体重の最小値を管理する。

    # 体重の管理用配列
    weight = [float('inf')] * N
    weight[0] = W[0]

    # キューには (燃料消費, 頂点, 体重) を入れる
    hq = [(0, 0, W[0])]

    while hq:
        fuel, u, wgt = heapq.heappop(hq)
        if dist[u] < fuel:
            continue
        # uから隣接頂点vへ移動
        for v in graph[u]:
            # 辺を通過するときの燃料消費は現在の体重wgt
            new_fuel = fuel + wgt
            # vに到達した時の体重は wgt + W[v]
            new_wgt = wgt + W[v]
            if dist[v] > new_fuel or (dist[v] == new_fuel and weight[v] > new_wgt):
                dist[v] = new_fuel
                weight[v] = new_wgt
                heapq.heappush(hq, (new_fuel, v, new_wgt))

    for d in dist:
        print(d)

if __name__ == "__main__":
    main()