import sys
input = sys.stdin.read

def max_c2c(test_cases):
    results = []
    for case in test_cases:
        N, writers = case
        total_c2c = 0
        for A, B, C in writers:
            div1 = min(A, B)  # Max Div.1 contests from this writer
            div2 = min(B, C)  # Max Div.2 contests from this writer
            total_c2c += div1 + div2
        results.append(total_c2c)
    return results

def main():
    data = input().splitlines()
    T = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(T):
        N = int(data[index])
        writers = []
        for i in range(N):
            A, B, C = map(int, data[index + 1 + i].split())
            writers.append((A, B, C))
        test_cases.append((N, writers))
        index += N + 1
    
    results = max_c2c(test_cases)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()