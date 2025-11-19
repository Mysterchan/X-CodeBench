from heapq import heappop, heappush

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

visited = set()
visited.add((0, 0, 0))
q = [(-a[0]*b[0] - b[0]*c[0] - c[0]*a[0], 0, 0, 0)]

for _ in range(k):
    val, i, j, m = heappop(q)
    
    if i + 1 < n:
        key = (i + 1, j, m)
        if key not in visited:
            visited.add(key)
            heappush(q, (-a[i+1]*b[j] - b[j]*c[m] - c[m]*a[i+1], i+1, j, m))
    
    if j + 1 < n:
        key = (i, j + 1, m)
        if key not in visited:
            visited.add(key)
            heappush(q, (-a[i]*b[j+1] - b[j+1]*c[m] - c[m]*a[i], i, j+1, m))
    
    if m + 1 < n:
        key = (i, j, m + 1)
        if key not in visited:
            visited.add(key)
            heappush(q, (-a[i]*b[j] - b[j]*c[m+1] - c[m+1]*a[i], i, j, m+1))

print(-val)