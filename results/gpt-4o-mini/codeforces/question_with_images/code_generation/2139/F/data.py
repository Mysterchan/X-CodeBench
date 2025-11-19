def calculate_slider_positions(t, test_cases):
    MOD = 10**9 + 7
    results = []

    for case in test_cases:
        n, m, q, a, operations = case
        contributions = [0] * n
        
        for i in range(q):
            op_index, x = operations[i]
            op_index -= 1  # Convert to zero-based index
            
            # We need to calculate the effective position of slider `op_index`
            # when moving to position `x`.
            initial_pos = a[op_index]
            if initial_pos < x:
                # Moving to right
                for j in range(op_index + 1, n):
                    if a[j] <= x:
                        x = a[j] - 1
                    else:
                        break
                # Update the position of slider `op_index` to new position
                contributions[op_index] += x

            else:
                # Moving to left
                for j in range(op_index - 1, -1, -1):
                    if a[j] >= x:
                        x = a[j] + 1
                    else:
                        break
                # Update position of slider `op_index`
                contributions[op_index] += x

        # Now, contributions contains the sums calculated for each slider
        for k in range(n):
            contributions[k] = contributions[k] * factorial(q) % MOD

        results.append(contributions)

    return results

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % (10**9 + 7)
    return result

# Input handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(t):
        n, m, q = map(int, data[index].split())
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        operations = []
        
        for __ in range(q):
            i, x = map(int, data[index].split())
            operations.append((i, x))
            index += 1
        
        test_cases.append((n, m, q, a, operations))

    results = calculate_slider_positions(t, test_cases)
    
    for res in results:
        print(" ".join(map(str, res)))