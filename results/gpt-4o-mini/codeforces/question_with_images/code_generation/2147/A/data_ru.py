def min_steps_to_reach_target(t, queries):
    results = []
    for x, y in queries:
        total_distance = x + y
        steps = 0
        current_length = 0
        
        while current_length < total_distance:
            steps += 1
            current_length += steps
        
        if current_length < total_distance or (current_length - total_distance) % 2 != 0:
            results.append(-1)
        else:
            results.append(steps)
    
    return results

# Input reading
t = int(input().strip())
queries = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Getting results
results = min_steps_to_reach_target(t, queries)

# Output results
for result in results:
    print(result)