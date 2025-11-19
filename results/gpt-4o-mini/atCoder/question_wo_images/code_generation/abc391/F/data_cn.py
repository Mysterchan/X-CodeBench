import sys
import heapq

input = sys.stdin.read
def main():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    A = list(map(int, data[2:n+2]))
    B = list(map(int, data[n+2:2*n+2]))
    C = list(map(int, data[2*n+2:3*n+2]))
    
    # Use a max heap to store the top K largest values
    max_heap = []
    
    # Calculate A_i * B_j + B_j * C_k + C_k * A_i for each combination
    for i in range(n):
        for j in range(n):
            value = A[i] * B[j]
            for k in range(n):
                current_value = value + B[j] * C[k] + C[k] * A[i]
                if len(max_heap) < k:
                    heapq.heappush(max_heap, current_value)
                else:
                    if current_value > max_heap[0]:
                        heapq.heapreplace(max_heap, current_value)

    # The K-th largest value will be the smallest in the max_heap
    print(max_heap[0])

if __name__ == "__main__":
    main()