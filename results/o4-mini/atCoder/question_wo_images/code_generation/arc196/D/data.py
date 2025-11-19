def can_satisfy_requirements(N, M, Q, people, queries):
    # Create an array to track the balance of stamina changes
    balance = [0] * (N + 1)

    # Process each person's stamina requirements
    for S, T in people:
        if S > T:
            S, T = T, S
        # The stamina must be positive in the range (S, T)
        balance[S] += 1
        balance[T] -= 1

    # Calculate the prefix sums to determine the number of people passing through each town
    for i in range(1, N + 1):
        balance[i] += balance[i - 1]

    # Check if any town has a non-positive balance
    for i in range(1, N + 1):
        if balance[i] < 0:
            return ["No"] * Q  # If any town has a non-positive balance, all queries are "No"

    # Prepare results for each query
    results = []
    for L, R in queries:
        # Check if all people in the range L to R can be satisfied
        min_balance = float('inf')
        for i in range(L - 1, R):
            S, T = people[i]
            if S > T:
                S, T = T, S
            # Check the balance in the range (S, T)
            min_balance = min(min_balance, min(balance[S + 1:T]))

        if min_balance > 0:
            results.append("Yes")
        else:
            results.append("No")

    return results

import sys
input = sys.stdin.read

data = input().splitlines()
N, M, Q = map(int, data[0].split())
people = [tuple(map(int, line.split())) for line in data[1:M + 1]]
queries = [tuple(map(int, line.split())) for line in data[M + 1:M + 1 + Q]]

results = can_satisfy_requirements(N, M, Q, people, queries)
print("\n".join(results))