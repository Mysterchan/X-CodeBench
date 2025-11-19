def minimize_dissatisfaction(T, cases):
    results = []
    
    for case in cases:
        N = case[0]
        intervals = case[1]
        
        # Sort intervals based on their arrival time L_i
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result array for seating arrangement
        P = [0] * N
        
        # To keep track of the seats that are occupied
        occupied = [False] * N
        
        for i in range(N):
            # Find the first available seat
            for seat in range(N):
                if not occupied[seat]:
                    P[i] = seat + 1  # Store 1-based index
                    occupied[seat] = True
                    break
        
        results.append(" ".join(map(str, P)))
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    intervals = []
    for j in range(N):
        L, R = map(int, data[index + j + 1].split())
        intervals.append((L, R))
    cases.append((N, intervals))
    index += N + 1

# Get results
results = minimize_dissatisfaction(T, cases)

# Print results
for result in results:
    print(result)