import sys

input = sys.stdin.read
def main():
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N, M = int(data[index]), int(data[index + 1])
        index += 2
        
        A = list(map(int, data[index:index + N]))
        index += N
        B = list(map(int, data[index:index + N]))
        index += N

        # Sort both arrays
        A.sort()
        B.sort()

        # Calculate the maximum for the minimum possible values
        min_max = 0
        for i in range(N):
            min_max = max(min_max, (A[i] + B[N - 1 - i]) % M)
        
        results.append(min_max)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

main()