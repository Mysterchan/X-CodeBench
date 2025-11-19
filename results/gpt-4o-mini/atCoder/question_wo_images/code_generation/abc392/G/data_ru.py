def count_good_triplets(N, S):
    S_set = set(S)
    count = 0
    
    for B in S:
        for A in range(1, B):
            C = 2 * B - A
            if C > B and C in S_set:
                count += 1
                
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    S = list(map(int, data[1:N+1]))
    
    result = count_good_triplets(N, S)
    print(result)