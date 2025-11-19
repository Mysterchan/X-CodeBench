n = int(input())
a = list(map(int, input().split()))

count = 1  # The original sequence

# For each potential L position
l = 0
while l < n - 1:
    # Skip consecutive identical values
    while l < n - 1 and a[l] == a[l + 1]:
        l += 1
    
    if l >= n - 1:
        break
    
    # Count distinct values to the right that differ from a[l]
    seen = set()
    for r in range(l + 1, n):
        if a[r] != a[l] and a[r] not in seen:
            seen.add(a[r])
            count += 1
    
    l += 1

print(count)