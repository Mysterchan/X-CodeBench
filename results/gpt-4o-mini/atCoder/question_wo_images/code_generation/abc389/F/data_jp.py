import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0

    N = int(data[index])
    index += 1
    
    contests = []
    for _ in range(N):
        L = int(data[index])
        R = int(data[index + 1])
        contests.append((L, R))
        index += 2
    
    Q = int(data[index])
    index += 1
    
    queries = []
    for _ in range(Q):
        queries.append(int(data[index]))
        index += 1
    
    # Prepare the rating increment array
    rating_increment = [0] * (500001)  # Using 500001 for easy indexing

    for L, R in contests:
        rating_increment[L] += 1
        if R + 1 < len(rating_increment):
            rating_increment[R + 1] -= 1

    # Prefix sum to get the total increments at each rating level
    for i in range(1, len(rating_increment)):
        rating_increment[i] += rating_increment[i - 1]

    results = []
    for query in queries:
        # Add the starting rating to the increment at that rating
        results.append(query + rating_increment[query])

    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()