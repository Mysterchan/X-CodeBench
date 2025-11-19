def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Find possible range for S
    max_val = 0
    for i in range(n):
        if A[i] != -1:
            max_val = max(max_val, A[i])
        if B[i] != -1:
            max_val = max(max_val, B[i])
    
    # Try different values of S
    # S should be at least max_val (so all required values are non-negative)
    # Try up to a reasonable upper bound
    for S in range(max_val, max_val + n + 1001):
        if check(n, A, B, S):
            print("Yes")
            return
    
    print("No")

def check(n, A, B, S):
    # Required A values for each position (based on B)
    required = []
    flexible_count = 0  # positions where B[i] = -1
    
    for i in range(n):
        if B[i] == -1:
            flexible_count += 1
        else:
            req = S - B[i]
            if req < 0:
                return False
            required.append(req)
    
    # Available A values
    available = []
    wildcard_a = 0  # count of -1 in A
    
    for i in range(n):
        if A[i] == -1:
            wildcard_a += 1
        else:
            available.append(A[i])
    
    # Try to match available with required
    # First match fixed A values with required values
    available_copy = available[:]
    required_copy = required[:]
    
    for val in available_copy[:]:
        if val in required_copy:
            required_copy.remove(val)
            available_copy.remove(val)
    
    # Now we have:
    # - available_copy: fixed A values not yet matched
    # - required_copy: required A values not yet satisfied
    # - wildcard_a: number of -1s in A
    # - flexible_count: number of -1s in B
    
    # Check if remaining can be satisfied
    # wildcard_a can be set to satisfy required_copy or match with flexible positions
    # Remaining available_copy must go to flexible positions
    
    unmatched_required = len(required_copy)
    unmatched_available = len(available_copy)
    
    # We need at least unmatched_required wildcards to satisfy requirements
    if wildcard_a < unmatched_required:
        return False
    
    # After satisfying requirements, remaining wildcards + unmatched_available 
    # must equal flexible_count
    if wildcard_a - unmatched_required + unmatched_available != flexible_count:
        return False
    
    return True

solve()