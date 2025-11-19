import sys
import threading
def main():
    import sys
    import heapq

    input = sys.stdin.readline
    INF = 10**18

    T = int(input())
    out = []
    for _ in range(T):
        line = input()
        while line.strip() == "":
            line = input()
        N = int(line)
        A0 = list(map(int, input().split()))
        # build with sentinels
        n2 = N + 2
        A = [INF] * n2
        for i in range(N):
            A[i+1] = A0[i]
        # linked list
        prev = [i-1 for i in range(n2)]
        nxt = [i+1 for i in range(n2)]
        prev[0] = 0
        nxt[n2-1] = n2-1
        removed = [False] * n2
        # heap of (value, index)
        heap = [(A[i], i) for i in range(1, N+1)]
        heapq.heapify(heap)
        interior = N
        ans = 0
        while interior > 1:
            x, i = heapq.heappop(heap)
            if removed[i] or A[i] != x:
                continue
            p = prev[i]
            n = nxt[i]
            px = A[p]
            nx = A[n]
            if x == nx:
                # merge i and n
                removed[n] = True
                interior -= 1
                # unlink n
                nxt[i] = nxt[n]
                prev[nxt[n]] = i
                # increase value
                x1 = x + 1
                A[i] = x1
                heapq.heappush(heap, (x1, i))
            else:
                # adjust i's value by insertions
                m = px if px < nx else nx
                ans += m - x
                A[i] = m
                heapq.heappush(heap, (m, i))
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()