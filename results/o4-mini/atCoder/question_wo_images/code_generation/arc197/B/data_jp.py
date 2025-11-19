import sys
input = sys.stdin.read

def max_score(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        total_sum = sum(A)
        max_score = 0
        
        for a in A:
            if a > total_sum / N:
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
    for result in results:
        print(result)

if __name__ == "__main__":
    main()