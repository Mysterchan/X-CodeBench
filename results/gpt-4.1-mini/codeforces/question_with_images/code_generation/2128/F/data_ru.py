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
        edges_r = [[] for __ in range(n+1)]
        l_arr = [0]*m
        r_arr = [0]*m

        for i in range(m):
            u,v,l,r = map(int, input().split())
            edges[u].append((v,l,r))
            edges[v].append((u,l,r))
            edges_r[u].append((v,r))
            edges_r[v].append((u,r))
            l_arr[i] = l
            r_arr[i] = r

        # Функция для вычисления минимальных расстояний с весами l_i (нижние границы)
        def dijkstra_lower():
            dist = [INF]*(n+1)
            dist[1] = 0
            hq = [(0,1)]
            while hq:
                cd,u = heapq.heappop(hq)
                if cd > dist[u]:
                    continue
                for (nx,l,r) in edges[u]:
                    nd = cd + l
                    if nd < dist[nx]:
                        dist[nx] = nd
                        heapq.heappush(hq,(nd,nx))
            return dist

        # Функция для вычисления минимальных расстояний с весами r_i (верхние границы)
        def dijkstra_upper():
            dist = [INF]*(n+1)
            dist[1] = 0
            hq = [(0,1)]
            while hq:
                cd,u = heapq.heappop(hq)
                if cd > dist[u]:
                    continue
                for (nx,r) in edges_r[u]:
                    nd = cd + r
                    if nd < dist[nx]:
                        dist[nx] = nd
                        heapq.heappush(hq,(nd,nx))
            return dist

        dist_l = dijkstra_lower()
        dist_r = dijkstra_upper()

        # Аналогично считаем dist от k и от n для нижних и верхних границ
        # Для dist_w(1,k) и dist_w(k,n) нам нужны минимальные и максимальные значения
        # Но для проверки условия достаточно проверить, можно ли сделать strict inequality

        # Для dist_w(1,k) минимальное и максимальное
        # Для dist_w(k,n) минимальное и максимальное

        # Чтобы получить dist_w(k,n), нужно построить граф с ребрами (u,v,l,r) и (v,u,l,r)
        # и запустить dijkstra от k

        # Для нижних границ от k
        def dijkstra_lower_from(start):
            dist = [INF]*(n+1)
            dist[start] = 0
            hq = [(0,start)]
            while hq:
                cd,u = heapq.heappop(hq)
                if cd > dist[u]:
                    continue
                for (nx,l,r) in edges[u]:
                    nd = cd + l
                    if nd < dist[nx]:
                        dist[nx] = nd
                        heapq.heappush(hq,(nd,nx))
            return dist

        # Для верхних границ от k
        def dijkstra_upper_from(start):
            dist = [INF]*(n+1)
            dist[start] = 0
            hq = [(0,start)]
            while hq:
                cd,u = heapq.heappop(hq)
                if cd > dist[u]:
                    continue
                for (nx,r) in edges_r[u]:
                    nd = cd + r
                    if nd < dist[nx]:
                        dist[nx] = nd
                        heapq.heappush(hq,(nd,nx))
            return dist

        dist_l_k = dijkstra_lower_from(k)
        dist_r_k = dijkstra_upper_from(k)

        # Теперь у нас есть:
        # dist_l[1..n], dist_r[1..n] - минимальные и максимальные расстояния от 1
        # dist_l_k[1..n], dist_r_k[1..n] - минимальные и максимальные расстояния от k

        # dist_w(1,n) может быть в диапазоне [dist_l[n], dist_r[n]]
        # dist_w(1,k) может быть в диапазоне [dist_l_k[k], dist_r_k[k]] (но dist_l_k[k] = 0, dist_r_k[k] = 0)
        # dist_w(k,n) может быть в диапазоне [dist_l_k[n], dist_r_k[n]]

        # Условие: существует w, что dist_w(1,n) != dist_w(1,k) + dist_w(k,n)

        # Рассмотрим минимальные суммы:
        # min_sum = dist_l_k[k] + dist_l_k[n] = 0 + dist_l_k[n] = dist_l_k[n]
        # max_sum = dist_r_k[k] + dist_r_k[n] = 0 + dist_r_k[n] = dist_r_k[n]

        # dist_w(1,n) в [dist_l[n], dist_r[n]]

        # Если для всех w: dist_w(1,n) == dist_w(1,k) + dist_w(k,n),
        # то диапазон dist_w(1,n) совпадает с диапазоном dist_w(1,k)+dist_w(k,n),
        # и они равны всегда.

        # Иначе, если диапазоны пересекаются, но не совпадают, можно подобрать веса,
        # чтобы неравенство выполнялось.

        # Проверим, равны ли диапазоны:
        # dist_w(1,n) ∈ [dist_l[n], dist_r[n]]
        # dist_w(1,k)+dist_w(k,n) ∈ [dist_l_k[k]+dist_l_k[n], dist_r_k[k]+dist_r_k[n]] = [dist_l_k[n], dist_r_k[n]]

        # Если эти интервалы совпадают и равны, то ответ NO, иначе YES.

        # Но dist_l_k[k] = dist_r_k[k] = 0, так как расстояние от k до k = 0.

        # Проверим равенство интервалов:
        # dist_l[n] == dist_l_k[n] и dist_r[n] == dist_r_k[n]

        # Если да, то NO, иначе YES.

        if dist_l[n] == dist_l_k[n] and dist_r[n] == dist_r_k[n]:
            print("NO")
        else:
            print("YES")

threading.Thread(target=main).start()