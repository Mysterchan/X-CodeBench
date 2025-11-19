def main():
    S = input().strip()
    n = len(S)
    ans = 0

    # For each position i where S[i] == 'A', try all possible equal steps d > 0
    for i in range(n):
        if S[i] != 'A':
            continue
        # j = i + d, k = i + 2*d
        max_d = (n - 1 - i) // 2
        for d in range(1, max_d + 1):
            j = i + d
            k = i + 2*d
            if S[j] == 'B' and S[k] == 'C':
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()