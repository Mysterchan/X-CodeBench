n = int(input())
s = list(map(int, input().split()))

# Convert to set for O(1) lookup
s_set = set(s)

count = 0

# For each element as the middle element B
for b in s:
    # We need to find pairs (A, C) where A < B < C and B - A = C - B
    # This means A + C = 2*B, or C = 2*B - A
    
    # We need A < B, so we check all possible values of A
    # For each A < B, we can compute C = 2*B - A
    # We need to check if C exists in the set and C > B
    
    # To avoid counting each triplet multiple times, we iterate through possible A values
    for a in s:
        if a < b:
            c = 2 * b - a
            if c > b and c in s_set:
                count += 1

print(count)