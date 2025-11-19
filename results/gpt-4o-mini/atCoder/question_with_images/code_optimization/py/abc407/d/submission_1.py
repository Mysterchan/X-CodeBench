import sys
from functools import reduce
from operator import xor

def main():
    input = sys.stdin.read
    data = input().split()
    
    h = int(data[0])
    w = int(data[1])
    
    aa = []
    index = 2
    for i in range(h):
        row = [int(data[index + j]) for j in range(w)]
        aa.append(row)
        index += w

    allxor = reduce(xor, (reduce(xor, row) for row in aa))

    # Dynamic Programming to find the maximum score
    dp = {}
    
    def dfs(mask, i, j):
        if (mask, i, j) in dp:
            return dp[(mask, i, j)]
        
        # Base case: reached the end of the grid
        if i >= h:
            return 0
        
        # Move to the next cell
        next_i, next_j = (i, j + 1) if (j + 1) < w else (i + 1, 0)
        
        # 1. Don't place any domino on (i, j)
        score = dfs(mask, next_i, next_j)  # continue without changing mask
        
        # 2. Try to place a domino horizontally if possible
        if j < w - 1 and not (mask & (1 << (i * w + j))):
            if not (mask & (1 << (i * w + (j + 1)))):
                new_mask = mask | (1 << (i * w + j)) | (1 << (i * w + (j + 1)))  # place horizontal domino
                score = max(score, dfs(new_mask, next_i, next_j))

        # 3. Try to place a domino vertically if possible
        if i < h - 1 and not (mask & (1 << (i * w + j))):
            if not (mask & (1 << (((i + 1) * w) + j))):
                new_mask = mask | (1 << (i * w + j)) | (1 << (((i + 1) * w) + j))  # place vertical domino
                score = max(score, dfs(new_mask, next_i, next_j))

        dp[(mask, i, j)] = score
        return score

    max_score = allxor
    max_score = max(max_score, dfs(0, 0, 0))  # Start with an empty mask
    print(max_score)

if __name__ == '__main__':
    main()