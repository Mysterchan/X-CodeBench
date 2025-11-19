def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    idx = 0
    H = int(data[idx])
    W = int(data[idx + 1])
    idx += 2
    
    A = []
    for h in range(H):
        A.append([int(data[idx + w]) for w in range(W)])
        idx += W
    
    Q = int(data[idx])
    sh = int(data[idx + 1]) - 1
    sw = int(data[idx + 2]) - 1
    idx += 3
    
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    
    def calculate_paths_sum():
        total_paths_sum = 0
        for i in range(H):
            for j in range(W):
                if i + j == sh + sw:
                    total_paths_sum += A[i][j]
                    total_paths_sum %= MOD
        return total_paths_sum
    
    results = []
    
    for _ in range(Q):
        d = data[idx]
        a = int(data[idx + 1])
        idx += 2
        
        # Move in the specified direction
        dh, dw = directions[d]
        sh += dh
        sw += dw
        
        # Update the grid
        A[sh][sw] = a
        
        # Calculate the sum of f(P)
        result = calculate_paths_sum()
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()