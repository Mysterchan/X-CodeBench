import sys
import threading

def main():
    import sys
    from collections import deque

    input = sys.stdin.readline
    N = int(input())
    C = [input().strip() for _ in range(N)]
    # Build incoming and outgoing adjacency by letter
    incoming = [ [ [] for _ in range(N) ] for _ in range(26) ]
    outgoing = [ [ [] for _ in range(N) ] for _ in range(26) ]
    for u in range(N):
        row = C[u]
        for v, ch in enumerate(row):
            if ch != '-':
                c = ord(ch) - 97
                outgoing[c][u].append(v)
                incoming[c][v].append(u)
    # dist[u][v] = minimal palindrome path length from u to v, or -1
    dist = [ [-1]*N for _ in range(N) ]
    dq = deque()
    # distance 0: (u,u)
    for u in range(N):
        dist[u][u] = 0
        dq.append((u, u))
    # distance 1: any direct edge u->v
    for u in range(N):
        for v, ch in enumerate(C[u]):
            if ch != '-' and dist[u][v] == -1:
                dist[u][v] = 1
                dq.append((u, v))
    # BFS on state graph with reversed transitions
    while dq:
        u1, v1 = dq.popleft()
        d1 = dist[u1][v1]
        nd = d1 + 2
        # For each letter, match incoming to u1 and outgoing from v1
        for c in range(26):
            in_list = incoming[c][u1]
            if not in_list:
                continue
            out_list = outgoing[c][v1]
            if not out_list:
                continue
            for u in in_list:
                row_u = dist[u]
                for v in out_list:
                    if row_u[v] == -1:
                        row_u[v] = nd
                        dq.append((u, v))
    # Output
    out = []
    for i in range(N):
        row = dist[i]
        out.append(" ".join(str(x) for x in row))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()