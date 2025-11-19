def main():
    S = input().strip()
    n = len(S)
    count = 0
    for i in range(n):
        if S[i] != 'A':
            continue
        # j = i + d, k = i + 2*d
        # ensure k < n
        max_d = (n - 1 - i) // 2
        for d in range(1, max_d + 1):
            if S[i + d] == 'B' and S[i + 2 * d] == 'C':
                count += 1
    print(count)

if __name__ == "__main__":
    main()