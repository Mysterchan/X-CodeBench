def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m, k = map(int, data[index].split())
        index += 1
        grid = [data[index + i] for i in range(n)]
        index += n
        
        gold = 0
        
        # Evaluating all possible explosion points
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '.':
                    # Calculate the boundaries of the explosive square
                    left = max(0, x - k)
                    right = min(n - 1, x + k)
                    top = max(0, y - k)
                    bottom = min(m - 1, y + k)

                    for i in range(left, right + 1):
                        for j in range(top, bottom + 1):
                            if grid[i][j] == 'g':
                                if left < i < right and top < j < bottom:
                                    # Inside the square, gold will disappear
                                    continue
                                gold += 1
        
        results.append(gold)

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solve()