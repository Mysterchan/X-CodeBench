def is_exit_possible(n, k, p, d, queries):
    signal_intervals = [(p[i], d[i] // k, d[i] % k) for i in range(n)]
    results = []
    
    for a in queries:
        pos = a
        direction = 1  # 1 for right, -1 for left
        step = 0
        
        while True:
            if pos in p:  # If there's a traffic light at the current position
                index = p.index(pos)
                light_timer = (step + d[index]) % k
                if light_timer == 0:
                    direction *= -1  # Turn around
            
            # Move to the next position
            pos += direction
            
            # Check for exit conditions
            if pos < 1:  # Exiting from the left side
                results.append("YES")
                break
            elif pos > 10**15:  # Exiting from the right side
                results.append("YES")
                break
            
            step += 1
            if step > 10**100:  # Safety net, theoretically shouldn't make it this far
                results.append("NO")
                break
        
    return results

import sys
input = sys.stdin.read

data = input().split()
index = 0
t = int(data[index])
index += 1
output = []

for _ in range(t):
    n, k = int(data[index]), int(data[index + 1])
    index += 2
    p = list(map(int, data[index:index + n]))
    index += n
    d = list(map(int, data[index:index + n]))
    index += n
    q = int(data[index])
    index += 1
    queries = list(map(int, data[index:index + q]))
    index += q

    results = is_exit_possible(n, k, p, d, queries)
    output.extend(results)

sys.stdout.write("\n".join(output) + "\n")