def assign_seats(num_cases, cases):
    results = []
    for n, times in cases:
        # Create a list of (L, R, index)
        events = [(times[i][0], times[i][1], i) for i in range(n)]
        # Sort by L ascending, then by R ascending
        events.sort()

        # Track assigned seats
        permutation = [0] * n
        assigned = [False] * n

        # Maintain a list of potentially available seats
        available_seats = list(range(1, n + 1))
        
        for L, R, i in events:
            # Find the smallest available seat
            for seat in available_seats:
                # If seat is available and assign it
                if not assigned[seat - 1]:
                    permutation[i] = seat
                    assigned[seat - 1] = True
                    break
        
        results.append(permutation)

    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
cases = []

line_index = 1
for _ in range(T):
    N = int(data[line_index])
    line_index += 1
    times = [tuple(map(int, data[line_index + i].split())) for i in range(N)]
    cases.append((N, times))
    line_index += N

results = assign_seats(T, cases)

for result in results:
    print(*result)