import sys

def II(): return int(input())
def LIIS(): return list(map(int,input().split()))

n = II()
A = LIIS()

if n % 2 == 0:
    A.sort()
    ans = sum(A[n//2:]) - sum(A[:n//2])
else:
    A.sort()
    # Precompute prefix sums for efficiency
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]
    
    ans = 0
    # Try removing each element at position i (only odd positions matter due to symmetry)
    for i in range(n):
        # Elements before i: 0..i-1 (i elements)
        # Elements after i: i+1..n-1 (n-i-1 elements)
        # Total: n-1 elements (even number)
        
        # Count how many from each side go to lower/upper half
        left_count = i
        right_count = n - i - 1
        total = left_count + right_count  # n-1
        half = total // 2
        
        if left_count >= half:
            # Lower half: A[0..half-1]
            # Upper half: A[half..i-1] + A[i+1..n-1]
            lower_sum = prefix[half]
            upper_sum = (prefix[i] - prefix[half]) + (prefix[n] - prefix[i+1])
        else:
            # Lower half: A[0..i-1] + A[i+1..i+1+(half-left_count)-1]
            # Upper half: A[i+1+(half-left_count)..n-1]
            needed = half - left_count
            lower_sum = prefix[i] + (prefix[i+1+needed] - prefix[i+1])
            upper_sum = prefix[n] - prefix[i+1+needed]
        
        score = upper_sum - lower_sum
        ans = max(ans, score)

print(ans)