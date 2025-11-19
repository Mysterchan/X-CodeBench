def can_transform(N, X, Y, S, T):
    # Convert strings to lists for easier manipulation
    S = list(S)
    T = list(T)

    # Check if we can transform S to T
    for i in range(N):
        if S[i] != T[i]:
            # If S[i] is 0 and T[i] is 1, we need to perform operation A
            if S[i] == '0' and T[i] == '1':
                # Check if we can perform operation A
                if i + X + Y <= N and all(S[j] == '0' for j in range(i, i + X)) and all(S[j] == '1' for j in range(i + X, i + X + Y)):
                    # Perform operation A
                    for j in range(i, i + Y):
                        S[j] = '1'
                    for j in range(i + Y, i + X):
                        S[j] = '0'
                else:
                    return "No"
            # If S[i] is 1 and T[i] is 0, we need to perform operation B
            elif S[i] == '1' and T[i] == '0':
                # Check if we can perform operation B
                if i + X + Y <= N and all(S[j] == '1' for j in range(i, i + Y)) and all(S[j] == '0' for j in range(i + Y, i + Y + X)):
                    # Perform operation B
                    for j in range(i, i + X):
                        S[j] = '0'
                    for j in range(i + X, i + X + Y):
                        S[j] = '1'
                else:
                    return "No"
    
    return "Yes" if S == T else "No"

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, X, Y = map(int, data[0].split())
S = data[1].strip()
T = data[2].strip()

# Get the result
result = can_transform(N, X, Y, S, T)

# Print the result
print(result)