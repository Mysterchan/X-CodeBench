import heapq
import sys
input = sys.stdin.readline

def solve(N, A):
    A = [10**18] + A + [10**18]
    ans = 0
    prev = [i-1 for i in range(N+2)]
    prev[0] = 0
    nxt = [i+1 for i in range(N+2)]
    nxt[N+1] = N+1
    
    heap = []
    for i in range(1, N+1):
        heapq.heappush(heap, (A[i], i))
    
    active = [True] * (N+2)
    active[0] = False
    active[N+1] = False
    
    while len(heap) > 1:
        while heap and not active[heap[0][1]]:
            heapq.heappop(heap)
        
        if len(heap) <= 1:
            break
            
        x, i = heapq.heappop(heap)
        
        if not active[i]:
            continue
            
        p = prev[i]
        n = nxt[i]
        px = A[p]
        nx = A[n]
        
        if x == nx:
            active[i] = False
            active[n] = False
            A[i] = x + 1
            nxt[i] = nxt[n]
            prev[nxt[n]] = i
            active[i] = True
            heapq.heappush(heap, (A[i], i))
        else:
            m = min(px, nx)
            ans += m - x
            A[i] = m
            heapq.heappush(heap, (m, i))
    
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(N, A))