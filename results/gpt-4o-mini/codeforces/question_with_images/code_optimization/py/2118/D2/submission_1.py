def process_traffic_lights(test_cases):
    results = []
    
    for n, k, positions, delays, queries in test_cases:
        # Build a mapping of positions and their delays
        lights = {positions[i]: delays[i] for i in range(n)}

        for a in queries:
            current_position = a
            direction = 1
            
            while True:
                if current_position < 1 or current_position > 10**15:
                    results.append("YES")
                    break
                
                if current_position in lights:
                    time = (current_position - 1) // k
                    next_red_time = time * k + lights[current_position]
                    
                    if ((current_position - 1) % k) == lights[current_position]:
                        direction *= -1
                    elif next_red_time < (10**100 + current_position - 1):
                        # if the next red happens before we can escape
                        time_until_red = next_red_time - (current_position - 1)
                        if time_until_red % 2 == 0:
                            direction *= -1
            
                current_position += direction
            
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))
    delays = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))
    test_cases.append((n, k, positions, delays, queries))

results = process_traffic_lights(test_cases)

for result in results:
    print(result)