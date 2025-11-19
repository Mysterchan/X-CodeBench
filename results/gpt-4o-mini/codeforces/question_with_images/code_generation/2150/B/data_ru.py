MOD = 998244353

def count_grids(n, a):
    sum_a = sum(a)
    
    if sum_a != n:
        return 0
        
    left_capacity = [0] * (n + 1)
    right_capacity = [0] * (n + 1)

    for i in range(1, n + 1):
        left_capacity[i] = n - a[i - 1]
        right_capacity[i] = n - a[i - 1]

    total_ways = 1
    
    for i in range(1, n + 1):
        if left_capacity[i] < 0 or right_capacity[i] < 0:
            return 0
        total_ways = total_ways * (left_capacity[i] + 1) % MOD
    
    return total_ways


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        results.append(count_grids(n, a))
    
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    main()