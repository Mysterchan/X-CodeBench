import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out_lines = []
    
    for _ in range(t):
        n, m = map(int, input().split())
        graph = defaultdict(list)
        
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        q = int(input().strip())
        queries = []
        for i in range(q):
            l, r, k = map(int, input().split())
            queries.append((l, r, k, i))

        ans = [0] * q
        
        for l, r, k, idx in queries:
            freq = [0] * (1 << 18)
            f_values = []
            for u in range(l, r + 1):
                xor_sum = 0
                for v in graph[u]:
                    if l <= v <= r:
                        xor_sum ^= v
                f_values.append(xor_sum)

            f_values.sort()
            ans[idx] = f_values[k - 1]

        out_lines.append('\n'.join(map(str, ans)))

    sys.stdout.write('\n'.join(out_lines) + '\n')

if __name__ == "__main__":
    main()