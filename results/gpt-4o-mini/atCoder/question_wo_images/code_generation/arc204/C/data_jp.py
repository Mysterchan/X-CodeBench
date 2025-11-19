def mex(x, y):
    return 0 if x != 0 and y != 0 else (1 if x != 1 and y != 1 else 2)

def calculate_score(N, P, A0, A1, A2):
    score = 0
    for i in range(N):
        b_i = 0 if i < A0 else (1 if i < A0 + A1 else 2)
        p_i = P[i] - 1  # Convert to 0-based index
        score += mex(b_i, P[p_i] - 1)  # P[p_i] is 1-based, convert to 0-based
    return score

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    P = list(map(int, data[index:index + N]))
    index += N
    Q = int(data[index])
    index += 1
    
    results = []
    for _ in range(Q):
        A0, A1, A2 = map(int, data[index:index + 3])
        index += 3
        score = calculate_score(N, P, A0, A1, A2)
        results.append(score)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()