import sys
input = sys.stdin.read

def max_score_subsequence(test_cases):
    results = []
    for A in test_cases:
        total_sum = sum(A)
        n = len(A)
        max_score = 0
        
        for i in range(n):
            if A[i] > total_sum / n:
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
        test_cases.append(A)
        index += 2
    
    results = max_score_subsequence(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()