def shortest_palindrome_paths(N, C):
    INF = float('inf')
    # Initialize the distance matrix
    dp = [[INF] * N for _ in range(N)]
    
    # Fill the distance matrix with initial edge lengths
    for i in range(N):
        for j in range(N):
            if C[i][j] != '-':
                dp[i][j] = 1
    
    # For a path from i to j that is a palindrome, we consider pairs (i -> k -> j)
    # such that the string formed by the edges is a palindrome.
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] != INF and dp[k][j] != INF:
                    # Check the middle character C[k][k] to make a palindrome
                    if C[k][k] != '-' and (C[i][k] == C[j][k] or (C[i][k] == '-' and C[j][k] == '-')):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (1 if C[k][k] != '-' else 0))

    # Generate the result table
    result = []
    for i in range(N):
        result.append(' '.join(str(dp[i][j]) if dp[i][j] != INF else '-1' for j in range(N)))
    
    return result

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  # Read the number of vertices
C = [data[i + 1].strip() for i in range(N)]  # Read the adjacency matrix (character representation)

# Function run and output
result = shortest_palindrome_paths(N, C)
for line in result:
    print(line)