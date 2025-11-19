def count_ways(N, H, W):
    MOD = 998244353
    
    # Calculate the number of ways to place 4 N x N tiles in H x W grid
    if H < N or W < N:
        return 0
    
    # Calculate the number of positions for the first tile
    positions_h = H - N + 1
    positions_w = W - N + 1
    
    # Total positions for 4 tiles
    total_positions = positions_h * positions_w
    
    # If there are not enough positions to place 4 tiles, return 0
    if total_positions < 4:
        return 0
    
    # Calculate the number of ways to choose 4 positions from total_positions
    # Using combinatorial formula: C(n, k) = n! / (k! * (n - k)!)
    # Here, we need C(total_positions, 4)
    
    # Calculate total_positions * (total_positions - 1) * (total_positions - 2) * (total_positions - 3) / 4!
    ways = (total_positions * (total_positions - 1) % MOD * (total_positions - 2) % MOD * (total_positions - 3) % MOD) * pow(24, MOD - 2, MOD) % MOD
    
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