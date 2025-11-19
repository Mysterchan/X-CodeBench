from heapq import heappop, heappush
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:n+2]))
b = list(map(int, data[n+2:2*n+2]))
c = list(map(int, data[2*n+2:3*n+2]))

# Sort the arrays in descending order
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

# Use a max-heap to keep track of the largest values
max_heap = []
visited = set()

# Push the initial combination into the heap
initial_value = a[0] * b[0] + b[0] * c[0] + c[0] * a[0]
heappush(max_heap, (-initial_value, 0, 0, 0))
visited.add((0, 0, 0))

# Extract the k-th largest value
for _ in range(k):
    neg_value, i, j, k = heappop(max_heap)
    current_value = -neg_value

    # Generate the next possible combinations
    if i + 1 < n and (i + 1, j, k) not in visited:
        visited.add((i + 1, j, k))
        new_value = a[i + 1] * b[j] + b[j] * c[k] + c[k] * a[i + 1]
        heappush(max_heap, (-new_value, i + 1, j, k))

    if j + 1 < n and (i, j + 1, k) not in visited:
        visited.add((i, j + 1, k))
        new_value = a[i] * b[j + 1] + b[j + 1] * c[k] + c[k] * a[i]
        heappush(max_heap, (-new_value, i, j + 1, k))

    if k + 1 < n and (i, j, k + 1) not in visited:
        visited.add((i, j, k + 1))
        new_value = a[i] * b[j] + b[j] * c[k + 1] + c[k + 1] * a[i]
        heappush(max_heap, (-new_value, i, j, k + 1))

# The k-th largest value is now stored in current_value
print(current_value)