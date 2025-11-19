def calculate_f(L, R, A):
    last_occurrence = {}
    unique_count = 0
    operations = 0
    
    for i in range(L, R + 1):
        if A[i] not in last_occurrence:
            unique_count += 1
        last_occurrence[A[i]] = i
    
    unique_count = len(last_occurrence)
    return unique_count

def calculate_sum_f(N, A):
    total_sum = 0
    for L in range(N):
        local_f_result = 0
        last_seen_count = {}
        unique_count = 0
        for R in range(L, N):
            if A[R] not in last_seen_count:
                unique_count += 1
            last_seen_count[A[R]] = R
            
            f_value = unique_count
            local_f_result += f_value
            
        total_sum += local_f_result
        
    return total_sum

N = int(input().strip())
A = list(map(int, input().strip().split()))

result = calculate_sum_f(N, A)
print(result)