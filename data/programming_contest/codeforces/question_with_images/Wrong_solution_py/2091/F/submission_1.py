import sys
import math

MOD = 998244353

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        d = int(input[ptr+2])
        ptr +=3
        grid = []
        for _ in range(n):
            grid.append(input[ptr])
            ptr +=1
        reversed_grid = grid[::-1]
        holds = []
        for row in reversed_grid:
            current_holds = []
            for j in range(m):
                if row[j] == 'X':
                    current_holds.append(j)
            holds.append(current_holds)
        dp_single = [ [0]*m for _ in range(n) ]
        dp_double = [ [0]*m for _ in range(n) ]
        current_row = 0
        current_holds = holds[current_row]
        for c in current_holds:
            dp_single[current_row][c] = 1
        is_hold = [0]*m
        for c in current_holds:
            is_hold[c] = 1
        prefix = [0]*(m+1)
        for i in range(m):
            prefix[i+1] = prefix[i] + is_hold[i]
        for c in current_holds:
            start = max(0, c - d)
            end = c - 1
            if start > end:
                dp_double[current_row][c] = 0
                continue
            count = prefix[end+1] - prefix[start]
            dp_double[current_row][c] = count % MOD
        for current_row in range(1, n):
            prev_row = current_row - 1
            current_holds = holds[current_row]
            prev_holds = holds[prev_row]
            comb_prev = [ (dp_single[prev_row][c] + dp_double[prev_row][c]) % MOD for c in range(m) ]
            prefix_comb = [0]*(m+1)
            for i in range(m):
                prefix_comb[i+1] = (prefix_comb[i] + comb_prev[i]) % MOD
            for c in current_holds:
                if d == 0:
                    left = c
                    right = c
                else:
                    K = int(math.isqrt(d*d -1))
                    left = max(0, c - K)
                    right = min(m-1, c + K)
                sum_val = (prefix_comb[right+1] - prefix_comb[left]) % MOD
                dp_single[current_row][c] = sum_val
            prefix_single = [0]*(m+1)
            for i in range(m):
                prefix_single[i+1] = (prefix_single[i] + dp_single[current_row][i]) % MOD
            for c in current_holds:
                start = max(0, c - d)
                end = c - 1
                if start > end:
                    dp_double[current_row][c] = 0
                    continue
                sum_val = (prefix_single[end+1] - prefix_single[start]) % MOD
                dp_double[current_row][c] = sum_val
        final_row = n-1
        total = 0
        for c in holds[final_row]:
            total = (total + dp_single[final_row][c] + dp_double[final_row][c]) % MOD
        print(total % MOD)

if __name__ == "__main__":
    main()
