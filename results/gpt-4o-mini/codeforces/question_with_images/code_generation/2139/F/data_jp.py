def simulate_sliders(t, test_cases):
    MOD = 10**9 + 7
    results = []

    for case in test_cases:
        n, m, q, initial_positions, operations = case
        final_sum = [0] * n

        for perm in range(1 << q):  # simulate all permutations of operations
            positions = initial_positions.copy()

            for j in range(q):
                op_index = (perm >> (j % q)) & 1
                i, x = operations[op_index]

                i -= 1  # convert to 0-index
                current_position = positions[i]
                
                while current_position < x:
                    moved = False
                    for k in range(i + 1, n):
                        if positions[k] <= current_position + 1:
                            current_position += 1
                            moved = True
                        else:
                            break
                    
                    if not moved:
                        for k in range(i - 1, -1, -1):
                            if positions[k] >= current_position - 1:
                                current_position -= 1
                            else:
                                break

                positions[i] = current_position
            
            for idx in range(n):
                final_sum[idx] = (final_sum[idx] + positions[idx]) % MOD

        results.append(final_sum)

    return results


# Read input
import sys
input = sys.stdin.read
data = input().strip().split('\n')

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, m, q = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    ops = []
    for _ in range(q):
        ops.append(tuple(map(int, data[index].split())))
        index += 1
    test_cases.append((n, m, q, a, ops))

# Get results
results = simulate_sliders(t, test_cases)

# Output results
for result in results:
    print(" ".join(map(str, result)))