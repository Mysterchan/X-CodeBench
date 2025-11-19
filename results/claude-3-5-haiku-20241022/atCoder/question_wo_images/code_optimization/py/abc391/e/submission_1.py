import sys

def main():
    N = int(input())
    A = input().strip()
    
    # Convert to list of integers for faster access
    values = [int(c) for c in A]
    costs = [1] * (3**N)
    
    for level in range(N):
        size = 3**(N - level)
        new_size = size // 3
        new_values = [0] * new_size
        new_costs = [0] * new_size
        
        for i in range(new_size):
            base = 3 * i
            # Count zeros in the triple
            zero_count = (1 - values[base]) + (1 - values[base + 1]) + (1 - values[base + 2])
            
            # Determine majority (0 if zero_count >= 2, else 1)
            if zero_count >= 2:
                new_values[i] = 0
                # Cost to flip to 1: sum of costs where value is 0, minus the max
                c0, c1, c2 = costs[base], costs[base + 1], costs[base + 2]
                if values[base] == 0:
                    if values[base + 1] == 0:
                        new_costs[i] = c0 + c1 - max(c0, c1)
                    elif values[base + 2] == 0:
                        new_costs[i] = c0 + c2 - max(c0, c2)
                    else:
                        new_costs[i] = c0
                elif values[base + 1] == 0:
                    if values[base + 2] == 0:
                        new_costs[i] = c1 + c2 - max(c1, c2)
                    else:
                        new_costs[i] = c1
                else:
                    new_costs[i] = c2
            else:
                new_values[i] = 1
                # Cost to flip to 0: sum of costs where value is 1, minus the max
                c0, c1, c2 = costs[base], costs[base + 1], costs[base + 2]
                if values[base] == 1:
                    if values[base + 1] == 1:
                        new_costs[i] = c0 + c1 - max(c0, c1)
                    elif values[base + 2] == 1:
                        new_costs[i] = c0 + c2 - max(c0, c2)
                    else:
                        new_costs[i] = c0
                elif values[base + 1] == 1:
                    if values[base + 2] == 1:
                        new_costs[i] = c1 + c2 - max(c1, c2)
                    else:
                        new_costs[i] = c1
                else:
                    new_costs[i] = c2
        
        values = new_values
        costs = new_costs
    
    print(costs[0])

if __name__ == "__main__":
    main()