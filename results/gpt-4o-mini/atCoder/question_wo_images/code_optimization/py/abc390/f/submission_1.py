def optimized_sum_f(N, A):
    last_position = {}
    f_values = [0] * (N + 1)
    
    for L in range(1, N + 1):
        current_count = 0
        current_set = set()
        
        for R in range(L, N + 1):
            if A[R - 1] not in current_set:
                current_set.add(A[R - 1])
                current_count += 1
            
            if A[R - 1] in last_position:
                f_values[L] += 1
            else:
                f_values[L] += current_count
            
            last_position[A[R - 1]] = R

    total_sum = sum(f_values[1:N + 1])
    return total_sum

N = int(input())
A = list(map(int, input().split()))
print(optimized_sum_f(N, A))