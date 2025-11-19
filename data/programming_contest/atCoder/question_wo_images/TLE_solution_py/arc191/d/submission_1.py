import sys
sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(1000000)
import sys
import heapq
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it)); m = int(next(it)); S = int(next(it))-1; T = int(next(it))-1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))-1; v = int(next(it))-1
        graph[u].append(v)
        graph[v].append(u)

    distT_arr = [-1] * n
    q_bfs = deque()
    distT_arr[T] = 0
    q_bfs.append(T)
    while q_bfs:
        u = q_bfs.popleft()
        for v in graph[u]:
            if distT_arr[v] == -1:
                distT_arr[v] = distT_arr[u] + 1
                q_bfs.append(v)

    distS_arr = [-1] * n
    q_bfs.append(S)
    distS_arr[S] = 0
    while q_bfs:
        u = q_bfs.popleft()
        for v in graph[u]:
            if distS_arr[v] == -1:
                distS_arr[v] = distS_arr[u] + 1
                q_bfs.append(v)

    dist_state = {}
    heap = []

    start = (S, T)
    g0 = 0
    h0 = max(distT_arr[S], distS_arr[T])
    f0 = g0 + h0
    heapq.heappush(heap, (f0, g0, S, T))
    dist_state[start] = g0

    while heap:
        f_val, moves, a, b = heapq.heappop(heap)
        if dist_state.get((a, b), 10**15) < moves:
            continue
        if a == T and b == S:
            print(moves)
            return

        for a_next in graph[a]:
            if a_next == b:
                continue
            new_state = (a_next, b)
            new_moves = moves + 1
            if new_state not in dist_state or new_moves < dist_state[new_state]:
                dist_state[new_state] = new_moves
                h_new = max(distT_arr[a_next], distS_arr[b])
                f_new = new_moves + h_new
                heapq.heappush(heap, (f_new, new_moves, a_next, b))

        for b_next in graph[b]:
            if a == b_next:
                continue
            new_state = (a, b_next)
            new_moves = moves + 1
            if new_state not in dist_state or new_moves < dist_state[new_state]:
                dist_state[new_state] = new_moves
                h_new = max(distT_arr[a], distS_arr[b_next])
                f_new = new_moves + h_new
                heapq.heappush(heap, (f_new, new_moves, a, b_next))

    print(-1)

if __name__ == "__main__":
    main()