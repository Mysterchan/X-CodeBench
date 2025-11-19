def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1

        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, data[index].split())
            graph[u].append(v)
            graph[v].append(u)
            index += 1

        q = int(data[index])
        index += 1

        for _ in range(q):
            l, r, k = map(int, data[index].split())
            index += 1

            f_values = []
            for u in range(l, r + 1):
                xor_value = 0
                for v in graph[u]:
                    if l <= v <= r:  # Only consider neighbors in the range [l, r]
                        xor_value ^= v
                f_values.append(xor_value)

            f_values.sort()
            results.append(f_values[k - 1])  # k-th smallest, k is 1-indexed

    sys.stdout.write('\n'.join(map(str, results)) + '\n')