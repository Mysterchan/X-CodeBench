def can_transform(N, X, Y, S, T):
    S = list(S)
    T = list(T)

    # Check if we can transform S to T
    for i in range(N):
        if S[i] != T[i]:
            if S[i] == '0' and T[i] == '1':
                # We need to perform operation A
                if i + X + Y <= N and all(S[j] == '0' for j in range(i, i + X)) and all(S[j] == '1' for j in range(i + X, i + X + Y)):
                    for j in range(i, i + Y):
                        S[j] = '1'
                    for j in range(i + Y, i + X + Y):
                        S[j] = '0'
                else:
                    return "No"
            elif S[i] == '1' and T[i] == '0':
                # We need to perform operation B
                if i + X + Y <= N and all(S[j] == '1' for j in range(i, i + Y)) and all(S[j] == '0' for j in range(i + Y, i + X + Y)):
                    for j in range(i, i + X):
                        S[j] = '0'
                    for j in range(i + X, i + X + Y):
                        S[j] = '1'
                else:
                    return "No"

    return "Yes" if S == T else "No"

# Input reading
N, X, Y = map(int, input().split())
S = input().strip()
T = input().strip()

# Output the result
print(can_transform(N, X, Y, S, T))