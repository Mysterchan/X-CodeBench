import sys

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    Ks = []
    dicts = []
    for _ in range(N):
        parts = input().split()
        k = int(parts[0])
        arr = list(map(int, parts[1:]))
        # In case the line was broken, read more if needed
        while len(arr) < k:
            arr += list(map(int, input().split()))
        cnt = {}
        for x in arr:
            cnt[x] = cnt.get(x, 0) + 1
        Ks.append(k)
        dicts.append(cnt)

    best_num = 0
    best_den = 1

    for i in range(N):
        fi = dicts[i]
        Ki = Ks[i]
        for j in range(i+1, N):
            fj = dicts[j]
            Kj = Ks[j]
            # iterate over smaller dict
            if len(fi) <= len(fj):
                small, large = fi, fj
            else:
                small, large = fj, fi
            num = 0
            for x, c in small.items():
                num += c * large.get(x, 0)
            if num == 0:
                continue
            den = Ki * Kj
            # compare num/den ? best_num/best_den  <=> num*best_den ? best_num*den
            if num * best_den > best_num * den:
                best_num = num
                best_den = den

    ans = best_num / best_den
    # print with sufficient precision
    print("{:.15f}".format(ans))

if __name__ == "__main__":
    main()