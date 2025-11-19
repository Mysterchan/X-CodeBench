N = int(input())
A = list(map(int, input().split()))

for year in range(1, N + 1):
    new_adult_idx = year - 1
    
    # Count adults with at least 1 stone (before this alien becomes adult)
    gift_count = 0
    for i in range(new_adult_idx):
        if A[i] >= 1:
            gift_count += 1
            A[i] -= 1
    
    # New adult receives gifts
    A[new_adult_idx] += gift_count

print(' '.join(map(str, A)))