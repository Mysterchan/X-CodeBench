import sys
import threading

def main():
    import sys
    data = sys.stdin
    N = int(data.readline())
    dice = []
    for _ in range(N):
        parts = data.readline().split()
        Ki = int(parts[0])
        faces = list(map(int, parts[1:]))
        freq = {}
        for v in faces:
            freq[v] = freq.get(v, 0) + 1
        dice.append((Ki, freq))

    best_num = 0
    best_den = 1

    # For each pair of dice, compute sum_n = sum over v of cnt_i * cnt_j
    for i in range(N):
        Ki, fi = dice[i]
        keys_i = fi.keys()
        len_i = len(keys_i)
        for j in range(i + 1, N):
            Kj, fj = dice[j]
            # iterate over smaller map
            if len_i <= len(fj):
                smaller, larger = fi, fj
            else:
                smaller, larger = fj, fi
            s = 0
            # s = sum cnt_smaller[v] * cnt_larger[v]
            for v, cnt_sm in smaller.items():
                cnt_lg = larger.get(v)
                if cnt_lg:
                    s += cnt_sm * cnt_lg
            if s == 0:
                continue
            den = Ki * Kj
            # compare s/den with best_num/best_den
            # s * best_den > best_num * den
            if s * best_den > best_num * den:
                best_num = s
                best_den = den

    # compute answer
    if best_num == 0:
        ans = 0.0
    else:
        ans = best_num / best_den
    # print with sufficient precision
    print("{:.15f}".format(ans))

if __name__ == "__main__":
    main()