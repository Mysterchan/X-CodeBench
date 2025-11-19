def function():
    import sys
    from itertools import combinations

    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))

    possible_xors = set()
    
    # Calculate all possible sums of subsets
    for r in range(N + 1):
        for combo in combinations(A, r):
            possible_xors.add(sum(combo))
    
    # The number of different possible values for the XOR
    print(len(possible_xors))

if __name__ == "__main__":
    function()