def calculate_f(N, A):
    total_operations = 0
    
    for L in range(N):
        last_seen = {}
        current_operations = 0
        left_distinct_count = 0
        
        for R in range(L, N):
            if A[R] not in last_seen:
                left_distinct_count += 1
                current_operations += 1
            last_seen[A[R]] = R
            
            if left_distinct_count > 0:
                last_latest_pos = -1
                initialization = left_distinct_count
                erase_operations = 0
                
                for j in range(L, R + 1):
                    if A[j] != -1:  # Mark the current number as still present
                        last_latest_pos = j
                    while last_latest_pos >= L and A[last_latest_pos] != -1:
                        last_latest_pos -= 1
                        erase_operations += 1
                        # Erase all occurrences of A[j]
                        for k in range(L, R + 1):
                            if A[k] == A[j]:
                                A[k] = -1  # Mark it as erased
                        left_distinct_count -= 1
                        if left_distinct_count <= 0:
                            break
                        
                    if left_distinct_count <= 0:
                        break
                
                current_operations += erase_operations
            
            total_operations += current_operations

    return total_operations


# Input reading
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N + 1]))

# Output
print(calculate_f(N, A))