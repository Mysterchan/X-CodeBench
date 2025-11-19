import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    
    A = list(map(int, data[2:N+2]))
    B = list(map(int, data[N+2:2*N+2]))
    C = list(map(int, data[2*N+2:3*N+2]))
    
    # To hold the maximum K elements we encountered
    max_heap = []
    
    # Using a min heap to keep track of the largest K elements
    for i in range(N):
        for j in range(N):
            # We compute a_b_c for every fixed A[i] and B[j]
            formulas = []
            for k in range(N):
                value = A[i] * B[j] + B[j] * C[k] + C[k] * A[i]
                formulas.append(value)
            
            # We only need the largest K values
            for value in formulas:
                if len(max_heap) < K:
                    heapq.heappush(max_heap, value)
                elif value > max_heap[0]:
                    heapq.heappushpop(max_heap, value)
    
    # The K-th largest value is the smallest in our max_heap
    print(max_heap[0])

if __name__ == "__main__":
    main()