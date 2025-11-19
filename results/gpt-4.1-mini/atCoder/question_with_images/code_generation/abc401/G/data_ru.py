import sys
import math
from collections import deque

def input():
    return sys.stdin.readline()

def can(t, dist, n):
    # Построим двудольный граф: люди -> кнопки
    # Ребро существует, если человек может дойти до кнопки за время <= t
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= t:
                graph[i].append(j)
    # Проверим, существует ли паросочетание размера n
    # Используем алгоритм Куна (DFS) для поиска максимального паросочетания
    match_to = [-1]*n

    def try_kuhn(v, used):
        for u in graph[v]:
            if used[u]:
                continue
            used[u] = True
            if match_to[u] == -1 or try_kuhn(match_to[u], used):
                match_to[u] = v
                return True
        return False

    result = 0
    for v in range(n):
        used = [False]*n
        if try_kuhn(v, used):
            result += 1
    return result == n

def main():
    sys.setrecursionlimit(10**7)
    n = int(sys.stdin.readline())
    sx = [0]*n
    sy = [0]*n
    for i in range(n):
        x,y = map(int, sys.stdin.readline().split())
        sx[i], sy[i] = x,y
    gx = [0]*n
    gy = [0]*n
    for i in range(n):
        x,y = map(int, sys.stdin.readline().split())
        gx[i], gy[i] = x,y

    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dx = sx[i] - gx[j]
            dy = sy[i] - gy[j]
            dist[i][j] = math.sqrt(dx*dx + dy*dy)

    left = 0.0
    right = 2e19  # достаточно большое число, учитывая ограничения

    for _ in range(100):
        mid = (left + right)/2
        if can(mid, dist, n):
            right = mid
        else:
            left = mid

    print(right)

if __name__ == "__main__":
    main()