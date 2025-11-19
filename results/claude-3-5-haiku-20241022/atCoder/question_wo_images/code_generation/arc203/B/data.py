def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Check if they have the same count of 0s and 1s
    if A.count(1) != B.count(1):
        return "No"
    
    # If already equal
    if A == B:
        return "Yes"
    
    # If all elements are the same (all 0s or all 1s)
    # Then we can only match if A == B (already checked)
    if A.count(1) == 0 or A.count(1) == n:
        return "No"
    
    # For sequences with both 0s and 1s, and same counts,
    # the operation is powerful enough to rearrange into any configuration
    return "Yes"

T = int(input())
for _ in range(T):
    print(solve())