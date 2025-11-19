import sys
sys.setrecursionlimit(100000)
MOD = 998244353

def count_permutations(n, s):
    # Count fixed and unfixed
    fixed_count = [0] * n
    unfixed_indices = []
    
    for i in range(n):
        if s[i] != -1:
            fixed_count[s[i]] += 1
        else:
            unfixed_indices.append(i)
    
    fixed_sum = sum(fixed_count)
    
    # Ensure that the number of fixed cells doesn't contradict scoring
    for i in range(n):
        if fixed_count[i] > i:
            return 0
    
    result = 1
    
    # Count available positions for remaining slots
    for idx in reversed(unfixed_indices):
        available_positions = idx - fixed_count[idx] - (fixed_sum - sum(fixed_count[:idx]))
        if available_positions <= 0:
            return 0
        result = (result * available_positions) % MOD
    
    # Calculate factorial for the permutations of unfixed indices
    from math import factorial
    result = (result * factorial(len(unfixed_indices))) % MOD

    return result

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index+n]))
        index += n
        res = count_permutations(n, s)
        results.append(str(res))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()