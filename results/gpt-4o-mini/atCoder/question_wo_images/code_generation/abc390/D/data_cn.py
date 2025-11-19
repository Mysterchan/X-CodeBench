def distinct_xor_count(N, A):
    possible_xors = set()
    total = sum(A)
    
    # Iterate through all possible combinations of bags
    for mask in range(1 << N):
        current_xor = 0
        current_sum = 0
        
        for i in range(N):
            if mask & (1 << i):  # If the i-th bag is chosen
                current_sum += A[i]
        
        current_xor = total - current_sum
        possible_xors.add(current_xor)
    
    return len(possible_xors)

# Input handling
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))
print(distinct_xor_count(N, A))