def solve(h, w, S):
    INF = float('inf')
    
    # Function to check if a 2x2 block in the bitmap is valid
    def check_valid(mask1, mask2):
        return (mask1 & 0b11) != 0 and (mask1 & 0b1100) != 0 and (mask2 & 0b11) != 0
    
    # Generate the initial state in bitmap form
    bitmaps = [(sum(1 << j for j in range(w) if S[i][j] == '#')) for i in range(h)]
    
    # DP array to store the minimum repaints needed for each line with a certain state
    dp = [[INF] * (1 << w) for _ in range(h)]
    
    # Process the first row
    for state in range(1 << w):
        count = bin(bitmaps[0] ^ state).count('1')
        dp[0][state] = count

    # Fill the DP table
    for i in range(1, h):
        for curr in range(1 << w):
            count = bin(bitmaps[i] ^ curr).count('1')
            for prev in range(1 << w):
                if check_valid(curr, prev):
                    dp[i][curr] = min(dp[i][curr], dp[i-1][prev] + count)
    
    # Find the minimum repaints needed for the last row
    return min(dp[h-1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        S = [input().strip() for _ in range(h)]
        print(solve(h, w, S))