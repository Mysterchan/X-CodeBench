import sys

input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])
    
    contests = []
    for i in range(1, N + 1):
        L, R = map(int, data[i].split())
        contests.append((L, R))
    
    Q = int(data[N + 1])
    queries = list(map(int, data[N + 2:N + 2 + Q]))
    
    # max value of X is 500000
    max_r = 500000
    rating_increments = [0] * (max_r + 2)
    
    for L, R in contests:
        rating_increments[L] += 1
        rating_increments[R + 1] -= 1
    
    # Compute prefix sum to determine total increments
    total_increments = [0] * (max_r + 1)
    current_increment = 0
    for i in range(1, max_r + 1):
        current_increment += rating_increments[i]
        total_increments[i] = current_increment
    
    results = []
    for X in queries:
        results.append(X + total_increments[X])
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()