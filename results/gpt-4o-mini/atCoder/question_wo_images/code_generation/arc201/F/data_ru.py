def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        
        # Initialize total counts for different divisions
        total_a = total_b = total_c = total_d = total_e = 0
        counts = []
        
        for i in range(N):
            A, B, C, D, E = map(int, data[index].split())
            index += 1
            
            total_a += A
            total_b += B
            total_c += C
            total_d += D
            total_e += E
            
            # Calculate maximum C3Cs for first i+1 authors
            div1_count = min(total_a, total_b, total_c)
            div2_count = min(total_b, total_c, total_d)
            div3_count = min(total_c, total_d, total_e)
            
            counts.append(str(div1_count + div2_count + div3_count))
        
        results.append(" ".join(counts))
    
    print("\n".join(results))

solve()