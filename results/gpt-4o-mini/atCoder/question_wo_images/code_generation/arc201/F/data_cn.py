import sys
input = sys.stdin.read

def max_c3c(N, proposals):
    result = []
    total_div1, total_div2, total_div3 = 0, 0, 0
    
    for k in range(N):
        A, B, C, D, E = proposals[k]
        total_div1 += min(A, B, C)
        total_div2 += min(B, C, D)
        total_div3 += min(C, D, E)
        
        max_c3c = min(total_div1, total_div2, total_div3)
        result.append(max_c3c)
    
    return result

def main():
    data = input().splitlines()
    index = 0
    T = int(data[index])
    index += 1
    output = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        proposals = []
        
        for _ in range(N):
            A, B, C, D, E = map(int, data[index].split())
            proposals.append((A, B, C, D, E))
            index += 1
            
        result = max_c3c(N, proposals)
        output.append(' '.join(map(str, result)))
    
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    main()