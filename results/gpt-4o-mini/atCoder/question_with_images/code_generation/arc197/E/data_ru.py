def count_ways(N, H, W):
    MOD = 998244353
    
    # Calculate the number of ways to place 4 N x N tiles in H x W grid
    if H < 2 * N or W < 2 * N:
        return 0
    
    # Calculate the number of positions for the first tile
    positions_h = H - N + 1
    positions_w = W - N + 1
    
    # Calculate the number of ways to choose 4 positions from the available positions
    total_positions = positions_h * positions_w
    
    if total_positions < 4:
        return 0
    
    # Calculate combinations C(total_positions, 4)
    from math import comb
    ways = comb(total_positions, 4) % MOD
    
    return ways

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N, H, W = map(int, data[i].split())
        result = count_ways(N, H, W)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()