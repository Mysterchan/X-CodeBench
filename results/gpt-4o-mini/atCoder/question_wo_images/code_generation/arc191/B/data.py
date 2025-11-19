def find_kth_compatible(N, K):
    compatible_numbers = []
    x = N
    while len(compatible_numbers) < K:
        if (x ^ N) % N == x % N:
            compatible_numbers.append(x)
        x += 1
    return compatible_numbers[K - 1] if len(compatible_numbers) >= K else -1

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
        result = find_kth_compatible(N, K)
        results.append(result)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()