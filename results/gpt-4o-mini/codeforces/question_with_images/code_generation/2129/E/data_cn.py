import sys
from collections import defaultdict
import bisect

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = defaultdict(list)
        
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        q = int(input())
        results = []
        
        for _ in range(q):
            l, r, k = map(int, input().split())
            f_values = []

            for u in range(l, r + 1):
                f_u = 0
                for v in graph[u]:
                    if l <= v <= r:
                        f_u ^= v
                f_values.append(f_u)

            f_values.sort()
            result = f_values[k - 1]
            results.append(result)

        print('\n'.join(map(str, results)))

main()