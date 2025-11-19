import sys
import threading
import heapq

def main():
    input = sys.stdin.readline
    t = int(input())
    INF = 10**15

    for _ in range(t):
        n, m, k = map(int, input().split())
        edges = [[] for __ in range(n+1)]
        edges_rev = [[] for __ in range(n+1)]
        l_arr = [0]*m
        r_arr = [0]*m

        for i in range(m):
            u,v,l,r = map(int, input().split())
            edges[u].append((v,l,r))
            edges[v].append((u,l,r))
            edges_rev[u].append((v,l,r))
            edges_rev[v].append((u,l,r))
            l_arr[i] = l
            r_arr[i] = r

        # Dijkstra with all edges at minimal weights
        def dijkstra(start, graph, use_min=True):
            dist = [INF]*(n+1)
            dist[start] = 0
            hq = [(0,start)]
            while hq:
                cd,u = heapq.heappop(hq)
                if cd > dist[u]:
                    continue
                for (nx,l,r) in graph[u]:
                    w = l if use_min else r
                    nd = cd + w
                    if nd < dist[nx]:
                        dist[nx] = nd
                        heapq.heappush(hq,(nd,nx))
            return dist

        # dist_min: all edges at minimal weights
        dist_min_1 = dijkstra(1, edges, True)
        dist_min_k = dijkstra(k, edges, True)
        dist_min_n = dijkstra(n, edges, True)

        # dist_max: all edges at maximal weights
        dist_max_1 = dijkstra(1, edges, False)
        dist_max_k = dijkstra(k, edges, False)
        dist_max_n = dijkstra(n, edges, False)

        # Check if for all weight assignments, dist(1,n) == dist(1,k)+dist(k,n)
        # If minimal dist(1,n) > maximal dist(1,k)+dist(k,n), then NO
        # If maximal dist(1,n) < minimal dist(1,k)+dist(k,n), then NO
        # Otherwise YES

        # minimal dist(1,n)
        d1n_min = dist_min_1[n]
        # maximal dist(1,n)
        d1n_max = dist_max_1[n]

        # minimal dist(1,k)+dist(k,n)
        d1k_min = dist_min_1[k]
        dkn_min = dist_min_k[n]
        d1k_dkn_min = d1k_min + dkn_min

        # maximal dist(1,k)+dist(k,n)
        d1k_max = dist_max_1[k]
        dkn_max = dist_max_k[n]
        d1k_dkn_max = d1k_max + dkn_max

        # If intervals [d1n_min, d1n_max] and [d1k_dkn_min, d1k_dkn_max] do not overlap,
        # then there exists a weight assignment making dist(1,n) != dist(1,k)+dist(k,n)
        # Otherwise, no.

        # Check if intervals overlap:
        # overlap if max(d1n_min, d1k_dkn_min) <= min(d1n_max, d1k_dkn_max)
        low = max(d1n_min, d1k_dkn_min)
        high = min(d1n_max, d1k_dkn_max)

        if low <= high:
            print("NO")
        else:
            print("YES")

threading.Thread(target=main).start()