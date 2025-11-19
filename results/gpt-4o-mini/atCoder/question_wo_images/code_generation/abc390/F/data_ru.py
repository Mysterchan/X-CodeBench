def calculate_sum_f(N, A):
    total_sum = 0
    for L in range(N):
        last_occurrence = {}
        unique_count = 0
        operations = 0
        
        for R in range(L, N):
            if A[R] not in last_occurrence:
                unique_count += 1
            last_occurrence[A[R]] = R
            
            if unique_count > operations:
                operations += 1
                
            # Remove operations for the current range
            for val in range(1, N + 1):
                if val in last_occurrence:
                    operations -= 1
                    break
            
            total_sum += operations
            
    return total_sum

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N + 1]))
    
    result = calculate_sum_f(N, A)
    print(result)