def solve(N, C):
    B = [0] * N
    total_stones = 0
    
    for i in range(N):
        total_stones += C[i]
        
        if i > 0:
            B[i] = max(0, C[i] + total_stones - (i + 1))
        else:
            B[i] = total_stones - (i + 1)
        
        total_stones -= min(C[i], total_stones)  # Adjust total stones after gifting
            
    return " ".join(map(str, B))

N = int(input())
C = list(map(int, input().split()))
print(solve(N, C))