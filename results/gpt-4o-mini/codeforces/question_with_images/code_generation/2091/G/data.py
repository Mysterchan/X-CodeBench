def max_power_after_journey(test_cases):
    results = []
    for s, k in test_cases:
        # The maximum distance Gleb can cover without turning is k * (k + 1) // 2.
        distance_without_turns = k * (k + 1) // 2
        
        # If the distance without turns is greater than or equal to s,
        # Gleb can reach point s without turning.
        if distance_without_turns >= s:
            results.append(k - (s - 1))
        else:
            # Otherwise, we need to reduce the power.
            # The remaining distance to cover after using up all his power 
            # is s - distance_without_turns.
            remaining_distance = s - distance_without_turns
            
            # Since Gleb has to turn around after reaching the maximum distance using his power,
            # he will use the max possible power he can exert in terms of k.
            # We can only turn as much as k - 1 times (due to power never reaching 0),
            # so the maximum power after reaching s is the rest from k minus the remaining distance.
            power_left = max(1, k - remaining_distance)
            results.append(power_left)
    
    return results

# Input handling
t = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Get results
outputs = max_power_after_journey(test_cases)

# Output results
for result in outputs:
    print(result)