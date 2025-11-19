def total_matches(n):
    # Each match results in one elimination until one team is left in losers' group.
    # To determine total matches, it's n - 1 for winners and (n-2) for those that drop to losers.
    return n - 1 + (n - 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Number of test cases
    results = []

    for i in range(1, t + 1):
        n = int(data[i])
        matches = total_matches(n)
        results.append(matches)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()