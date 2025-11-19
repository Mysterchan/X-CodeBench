import sys
import math

def can(t, dist, n):
    # t秒以内に移動可能な距離で辺を張った二部グラフで完全マッチングが存在するか判定
    # dist[i][j] <= t なら i番目の高橋くんはj番目のボタンに行ける
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= t:
                graph[i].append(j)

    matchR = [-1] * n

    def bpm(u, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    result = 0
    for i in range(n):
        seen = [False] * n
        if bpm(i, seen):
            result += 1
    return result == n

def main():
    input = sys.stdin.readline
    N = int(input())
    sx = [0]*N
    sy = [0]*N
    for i in range(N):
        x,y = map(int,input().split())
        sx[i], sy[i] = x,y
    gx = [0]*N
    gy = [0]*N
    for i in range(N):
        x,y = map(int,input().split())
        gx[i], gy[i] = x,y

    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dx = sx[i] - gx[j]
            dy = sy[i] - gy[j]
            dist[i][j] = math.sqrt(dx*dx + dy*dy)

    left = 0.0
    right = 2e19  # 十分大きな値
    for _ in range(100):
        mid = (left + right) / 2
        if can(mid, dist, N):
            right = mid
        else:
            left = mid

    print(right)

if __name__ == "__main__":
    main()