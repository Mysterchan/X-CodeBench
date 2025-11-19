def calculate_f(a):
    m = len(a)
    if m == 0:
        return 0
        
    max_height = 0
    operations = 0
    
    for i in range(m):
        max_height = max(max_height, a[i])
        operations += max_height
    
    return operations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        
        total_sum = 0
        
        for l in range(n):
            current_max = 0
            for r in range(l, n):
                current_max = max(current_max, a[r])
                total_sum = (total_sum + current_max) % MOD
        
        results.append(total_sum)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()