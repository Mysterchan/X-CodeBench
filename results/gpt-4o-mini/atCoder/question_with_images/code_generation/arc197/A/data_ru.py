def max_black_cells(H, W, S):
    # Count the number of D and R in S
    count_D = S.count('D')
    count_R = S.count('R')
    
    # The number of '?' can be used to fill the remaining moves
    count_Q = S.count('?')
    
    # The maximum number of D's we can use is H-1
    # The maximum number of R's we can use is W-1
    max_D = min(count_D + count_Q, H - 1)
    max_R = min(count_R + count_Q, W - 1)
    
    # The total number of cells that can be painted black
    return max_D + max_R + 1  # +1 for the starting cell (1,1)

import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        H, W = map(int, data[index].split())
        S = data[index + 1]
        index += 2
        
        result = max_black_cells(H, W, S)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()