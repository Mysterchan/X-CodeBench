MOD = 998244353

def count_permutations(n, s):
    fixed_counts = [0] * n
    fixed_positions = []
    for idx, value in enumerate(s):
        if value != -1:
            fixed_counts[value] += 1
            fixed_positions.append(idx)
    
    required_black = [0] * n
    for idx in range(n):
        if fixed_counts[idx] > 1:
            return 0
    
    for idx in range(n - 1):
        if s[idx] != -1 and (idx + 1) < n:
            required_black[idx + 1] = s[idx]

    total_permutations = 1
    for idx in range(n):
        if fixed_counts[idx] > 0:
            total_permutations = total_permutations * fixed_counts[idx] % MOD
        elif s[idx] == -1:
            total_permutations = total_permutations * (n - len(fixed_positions) - idx) % MOD

    return total_permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    t = int(data[0])
    output = []
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        s = list(map(int, data[index + 1].split()))
        index += 2
        result = count_permutations(n, s)
        output.append(result)
    
    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()