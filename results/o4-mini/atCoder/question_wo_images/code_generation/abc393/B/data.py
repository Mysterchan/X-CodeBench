def main():
    S = input().strip()
    N = len(S)
    count = 0
    
    # We look for triples (i, j, k) such that
    # S[i] == 'A', S[j] == 'B', S[k] == 'C', and j - i == k - j.
    # Equivalently, k = 2*j - i.
    for i in range(N):
        if S[i] != 'A':
            continue
        for j in range(i + 1, N):
            if S[j] != 'B':
                continue
            k = 2 * j - i
            if k < N and S[k] == 'C':
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()