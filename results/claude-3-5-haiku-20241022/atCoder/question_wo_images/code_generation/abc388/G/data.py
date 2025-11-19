def solve_query(mochi):
    n = len(mochi)
    if n < 2:
        return 0
    
    # Try to pair mochi greedily
    used = [False] * n
    count = 0
    
    # For each mochi from smallest to largest, try to find a valid partner
    for i in range(n):
        if used[i]:
            continue
        # Find the smallest unused mochi j > i where mochi[i] <= mochi[j] / 2
        for j in range(i + 1, n):
            if not used[j] and 2 * mochi[i] <= mochi[j]:
                used[i] = True
                used[j] = True
                count += 1
                break
    
    return count

n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    mochi = A[l-1:r]  # Convert to 0-indexed
    print(solve_query(mochi))