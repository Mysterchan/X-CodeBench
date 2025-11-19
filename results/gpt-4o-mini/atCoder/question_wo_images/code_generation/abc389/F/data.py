import sys
from bisect import bisect_left, bisect_right

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    N = int(data[index])
    index += 1
    
    contests = []
    
    for _ in range(N):
        L, R = map(int, data[index].split())
        contests.append((L, R))
        index += 1
    
    Q = int(data[index])
    index += 1
    
    queries = []
    for _ in range(Q):
        X = int(data[index])
        queries.append(X)
        index += 1
    
    # Process contests to create boundaries for later use
    limits = []
    for L, R in contests:
        limits.append((L, 1))  # increment start
        limits.append((R + 1, -1))  # decrement after end
    
    # Sort limits based on the rating
    limits.sort()
    
    # Create a prefix sum to calculate increments
    increment_count = [0] * (500001)
    
    current_increment = 0
    last_limit = 0
    
    for value, change in limits:
        # Apply the current increment to all ratings between last_limit and value
        if last_limit < value:
            for i in range(last_limit, value):
                increment_count[i] = current_increment
            last_limit = value
            
        current_increment += change
    
    # Fill up to the maximum rating
    for i in range(last_limit, 500001):
        increment_count[i] = current_increment
    
    results = []
    for x in queries:
        results.append(x + increment_count[x])
    
    # Print all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()