import sys
def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    P = [int(next(it)) - 1 for _ in range(n * k)]
    visited = [False] * (n * k)
    ans = 0

    for start in range(n * k):
        if not visited[start]:
            # Traverse the cycle starting at 'start'
            cur = start
            size = 0
            cols = set()
            while not visited[cur]:
                visited[cur] = True
                cols.add(cur % n)
                size += 1
                cur = P[cur]
            # In a cycle of length size, maximum same-column swaps in the spanning tree
            # = size - (# distinct columns in this cycle)
            if size > 1:
                ans += size - len(cols)

    print(ans)

if __name__ == "__main__":
    main()