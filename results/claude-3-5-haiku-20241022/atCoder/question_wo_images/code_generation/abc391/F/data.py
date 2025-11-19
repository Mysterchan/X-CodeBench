import heapq

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    # Sort arrays in descending order for easier max-heap simulation
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    
    # Use a max heap (negate values for Python's min heap)
    # State: (negative_value, i, j, k)
    heap = []
    visited = set()
    
    # Start with the maximum possible value
    initial_val = A[0] * B[0] + B[0] * C[0] + C[0] * A[0]
    heapq.heappush(heap, (-initial_val, 0, 0, 0))
    visited.add((0, 0, 0))
    
    count = 0
    result = 0
    
    while heap and count < K:
        neg_val, i, j, k = heapq.heappop(heap)
        val = -neg_val
        count += 1
        
        if count == K:
            result = val
            break
        
        # Generate next candidates by incrementing i, j, or k
        for ni, nj, nk in [(i+1, j, k), (i, j+1, k), (i, j, k+1)]:
            if ni < N and nj < N and nk < N and (ni, nj, nk) not in visited:
                next_val = A[ni] * B[nj] + B[nj] * C[nk] + C[nk] * A[ni]
                heapq.heappush(heap, (-next_val, ni, nj, nk))
                visited.add((ni, nj, nk))
    
    print(result)

solve()