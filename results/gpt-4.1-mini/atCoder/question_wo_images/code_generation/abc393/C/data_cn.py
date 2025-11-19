import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_count = {}
remove_count = 0

for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        # self-loop must be removed
        remove_count += 1
    else:
        a, b = (u, v) if u < v else (v, u)
        if (a, b) in edge_count:
            # duplicate edge must be removed
            remove_count += 1
        else:
            edge_count[(a, b)] = 1

print(remove_count)