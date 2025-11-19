import sys
input = sys.stdin.read

def max_score(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        total_sum = sum(a)
        max_score = 0
        
        for num in a:
            if num > total_sum / n:
                max_score += 1
        
        results.append(max_score)
    
    return results

def main():
    data = input().splitlines()
    T = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])
        A = list(map(int, data[index + 1].split()))
        test_cases.append((N, A))
        index += 2
    
    results = max_score(test_cases)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()