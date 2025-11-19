import sys

input = sys.stdin.read

def max_perfect_records(test_cases):
    results = []
    for N, M in test_cases:
        results.append(M * (N // 2))
    return results

def main():
    data = input().strip().split()
    T = int(data[0])
    index = 1
    test_cases = []
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        test_cases.append((N, M))
        index += 2
        
    results = max_perfect_records(test_cases)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()