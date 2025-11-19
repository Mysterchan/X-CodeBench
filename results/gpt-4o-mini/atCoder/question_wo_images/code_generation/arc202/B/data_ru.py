def count_knight_tours(H, W):
    MOD = 998244353
    
    if (H + W) % 2 == 1 or min(H, W) < 3:
        return 0
    
    knights = H * W
    ans = 1
    
    for i in range(1, knights):
        ans = ans * (knights - i) % MOD
    
    return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    H, W = map(int, input().strip().split())
    print(count_knight_tours(H, W))