def main():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        grid = [input().rstrip() for _ in range(n)]
        
        gold_positions = []
        total_gold = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'g':
                    gold_positions.append((r, c))
                    total_gold += 1
        
        max_gold = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '.':
                    collected = 0
                    for gr, gc in gold_positions:
                        if r - k <= gr <= r + k and c - k <= gc <= c + k:
                            if abs(gr - r) == k or abs(gc - c) == k:
                                collected += 1
                    max_gold = max(max_gold, collected)
        
        print(total_gold - max_gold)

if __name__ == "__main__":
    main()