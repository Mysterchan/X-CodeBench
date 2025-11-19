def find_kth_compatible_number(N, K):
    compatible_numbers = []
    for X in range(1, 2 * N + 1):
        if (X ^ N) % N == X % N:
            compatible_numbers.append(X)
            if len(compatible_numbers) == K:
                return X
    return -1

import sys
input = sys.stdin.read

def main():
    data = input().split()
    T = int(data[0])
    results = []
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        result = find_kth_compatible_number(N, K)
        results.append(result)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()