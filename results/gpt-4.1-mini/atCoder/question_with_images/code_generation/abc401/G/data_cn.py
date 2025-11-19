import sys
import math
from collections import deque

def can(t, dist, N):
    # 建立二分圖，判斷是否存在完美匹配
    # dist[i][j] <= t 表示第 i 個人能在時間 t 內到達第 j 個按鈕
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] <= t:
                graph[i].append(j)

    matchR = [-1] * N  # 按鈕匹配的人員

    def bpm(u, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    result = 0
    for i in range(N):
        seen = [False] * N
        if bpm(i, seen):
            result += 1
    return result == N

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
            dist[i][j] = math.hypot(dx, dy)

    left = 0.0
    right = 2e19  # 足夠大的上界
    for _ in range(100):
        mid = (left + right) / 2
        if can(mid, dist, N):
            right = mid
        else:
            left = mid

    print(right)

if __name__ == "__main__":
    main()