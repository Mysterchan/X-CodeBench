t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    results = []
    
    for _ in range(m):
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        
        # Update the number of missing bags after the flights
        current_bags = s[:]
        
        # For each airport, calculate maximum bags that can be sent out
        for j in range(n):
            bags_to_prev = min(a[j], current_bags[j])
            bags_to_next = min(c[j], current_bags[j])
            current_bags[j] -= (bags_to_prev + bags_to_next)
        
        # Calculate found luggage
        found_bags = 0
        for j in range(n):
            if current_bags[j] >= b[j]:
                found_bags += (current_bags[j] - b[j])
        
        # Bags that remain missing are the original bags minus found bags
        remaining_missing = sum(s) - found_bags
        results.append(remaining_missing)

        # Prepare for the next day's starting point
        for j in range(n):
            s[j] = current_bags[j] + sum(a[(j + 1) % n]) + sum(c[(j - 1) % n])

    print(" ".join(map(str, results)))