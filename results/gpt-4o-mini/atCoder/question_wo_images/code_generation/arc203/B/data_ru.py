def can_transform_to_b(test_cases):
    results = []
    for A, B in test_cases:
        if sum(A) != sum(B):
            results.append("No")
        else:
            results.append("Yes")
    return results

import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    T = int(data[0])
    test_cases = []
    index = 1
    for _ in range(T):
        N = int(data[index])
        A = list(map(int, data[index + 1].split()))
        B = list(map(int, data[index + 2].split()))
        test_cases.append((A, B))
        index += 3
    
    results = can_transform_to_b(test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()