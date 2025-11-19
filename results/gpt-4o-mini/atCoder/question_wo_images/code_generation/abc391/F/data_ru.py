import sys
import heapq

input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:N+2]))
    B = list(map(int, data[N+2:2*N+2]))
    C = list(map(int, data[2*N+2:3*N+2]))
    
    # Use a max heap to store the largest K values found
    max_heap = []
    
    # Iterate through each combination of i and j
    for i in range(N):
        for j in range(N):
            # Compute the base value for the current (A[i], B[j])
            base_value = A[i] * B[j]
            # Store a list of tuples (value, k_index) for each k_index in C
            # This is the value for each k
            for k in range(N):
                value = base_value + B[j] * C[k] + C[k] * A[i]
                if len(max_heap) < K:
                    heapq.heappush(max_heap, value)
                else:
                    # Only push if the new value is greater than the smallest in the heap
                    if value > max_heap[0]:
                        heapq.heappop(max_heap)
                        heapq.heappush(max_heap, value)
    
    # The K-th largest value is now at the root of the max_heap (smallest in max_heap)
    print(max_heap[0])

if __name__ == "__main__":
    main()