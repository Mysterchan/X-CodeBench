def count_arrangements(n, m, parents, colors, depths):
    MOD = 998244353

    # Step 1: Calculate the number of pieces for each depth
    count_by_depth = [0] * (n + 1)
    for d in depths:
        count_by_depth[d - 1] += 1

    # Step 2: Calculate total factorials and inverse factorials
    max_factorial = 2 * (sum(count_by_depth))
    factorial = [1] * (max_factorial + 1)
    inverse_factorial = [1] * (max_factorial + 1)
    
    for i in range(2, max_factorial + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    
    def mod_inverse(x, mod):
        return pow(x, mod - 2, mod)

    for i in range(max_factorial + 1):
        inverse_factorial[i] = mod_inverse(factorial[i], MOD)

    # Step 3: Counting the arrangements based on the colors
    total_arrangements = factorial[m]
    color_count = [0, 0]  # color_count[0] for black, color_count[1] for white

    for color in colors:
        color_count[color] += 1

    for count in color_count:
        total_arrangements *= inverse_factorial[count]
        total_arrangements %= MOD

    # Step 4: Calculate the final result
    result = total_arrangements
    for depth in count_by_depth:
        if depth > 0:
            result *= factorial[depth]
            result %= MOD

    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        parents = list(map(int, data[index].split()))
        index += 1
        colors = list(map(int, data[index].split()))
        index += 1
        depths = list(map(int, data[index].split()))
        index += 1
        
        result = count_arrangements(n, m, parents, colors, depths)
        results.append(result)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()