def is_good_string(N, A):
    if all(a == 1 for a in A):
        return "Yes"
    
    if A.count(0) < 2:
        return "No"
    
    for i in range(N):
        if A[i] == 0 and A[(i + 1) % N] == 0:
            return "Yes"
    
    return "No"

N = int(input().strip())
A = list(map(int, input().strip().split()))
print(is_good_string(N, A))