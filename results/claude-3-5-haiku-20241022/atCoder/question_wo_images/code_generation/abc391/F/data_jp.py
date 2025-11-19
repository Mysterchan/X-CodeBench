import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

heap = []
visited = set()

def calc_value(i, j, k):
    return A[i] * B[j] + B[j] * C[k] + C[k] * A[i]

heapq.heappush(heap, (-calc_value(0, 0, 0), 0, 0, 0))
visited.add((0, 0, 0))

count = 0
result = 0

while heap and count < K:
    neg_val, i, j, k = heapq.heappop(heap)
    result = -neg_val
    count += 1
    
    if count == K:
        break
    
    if i + 1 < N and (i + 1, j, k) not in visited:
        visited.add((i + 1, j, k))
        heapq.heappush(heap, (-calc_value(i + 1, j, k), i + 1, j, k))
    
    if j + 1 < N and (i, j + 1, k) not in visited:
        visited.add((i, j + 1, k))
        heapq.heappush(heap, (-calc_value(i, j + 1, k), i, j + 1, k))
    
    if k + 1 < N and (i, j, k + 1) not in visited:
        visited.add((i, j, k + 1))
        heapq.heappush(heap, (-calc_value(i, j, k + 1), i, j, k + 1))

print(result)