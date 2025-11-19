import sys
input = sys.stdin.read

def max_c2c(test_cases):
    results = []
    for case in test_cases:
        n, problems = case
        total_div1 = total_div2 = 0
        
        for a, b, c in problems:
            div1_possible = min(a, b)
            div2_possible = min(b, c)

            total_div1 += div1_possible
            total_div2 += div2_possible

        l, h = 0, 2 * (10 ** 14) + 5
        while h - l > 1:
            m = (l + h) // 2
            current_div1 = current_div2 = 0
            
            for a, b, c in problems:
                remaining_div1 = min(b - (m - current_div1), a)
                current_div1 += remaining_div1
                a -= remaining_div1
                b -= remaining_div1
                
                remaining_div2 = min(b, c)
                current_div2 += remaining_div2
            
            if current_div1 >= m and current_div2 >= m:
                l = m
            else:
                h = m
        
        results.append(l)
    
    return results

def main():
    data = input().strip().split('\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    test_cases = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        problems = []
        for _ in range(N):
            A, B, C = map(int, data[idx].split())
            problems.append((A, B, C))
            idx += 1
        test_cases.append((N, problems))
    
    results = max_c2c(test_cases)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()