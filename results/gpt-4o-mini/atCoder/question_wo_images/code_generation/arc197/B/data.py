import sys
input = sys.stdin.read

def max_score_subsequence(test_cases):
    results = []
    for A in test_cases:
        N = len(A)
        total_sum = sum(A)
        max_score = 0
        
        # Calculate the average
        average = total_sum / N
        
        # Count how many elements are greater than the average
        for num in A:
            if num > average:
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