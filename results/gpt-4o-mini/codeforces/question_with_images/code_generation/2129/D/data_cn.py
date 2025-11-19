MOD = 998244353

def count_permutations(n, s):
    # Initial variables
    color_count = [0] * n
    fixed_count = 0
    unknown_count = 0
    for score in s:
        if score != -1:
            fixed_count += 1
            color_count[score] += 1
        else:
            unknown_count += 1
            
    # Check constraints
    for i in range(n):
        if color_count[i] > 1:
            return 0
            
    # Validate scores
    for i in range(n):
        if s[i] != -1:
            if not (0 <= s[i] < n):
                return 0
            
            if color_count[s[i]] == 1:
                continue
            
            # If s[i] has a score > 0, it must have a black cell as well.
            if s[i] > 0:
                # The number of black cells to the left must be >= s[i].
                left_black_count = sum(color_count[:s[i]])
                if left_black_count < s[i]:
                    return 0
            
            # If s[i] is 0, it must be at the left-most side
            # If it's the right-most cell, it should be invalid if not filled.
            if i == n - 1 and s[i] != 0:
                return 0
            
    # Count ways to arrange unknowns
    from math import factorial
    
    # The number of ways we can place unknowns in available slots
    available_slots = n - fixed_count
    return factorial(available_slots) % MOD

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    results.append(count_permutations(n, s))

print('\n'.join(map(str, results)))