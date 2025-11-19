import heapq

N, M = map(int, input().split())
P = list(map(int, input().split()))

# Use a min-heap to always buy from the cheapest option
# Each element is (cost, product_index, current_count)
heap = [(p, i, 1) for i, p in enumerate(P)]
heapq.heapify(heap)

total_cost = 0
total_units = 0

while heap:
    cost, idx, count = heapq.heappop(heap)
    
    if total_cost + cost <= M:
        total_cost += cost
        total_units += 1
        
        # Add the next unit of this product to the heap
        next_count = count + 1
        next_cost = next_count * next_count * P[idx]
        heapq.heappush(heap, (next_cost, idx, next_count))
    else:
        break

print(total_units)