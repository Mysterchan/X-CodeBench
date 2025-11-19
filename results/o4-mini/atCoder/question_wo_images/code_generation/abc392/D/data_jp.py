import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    dice = []  # Each element: (K_i, Counter dict of face->count)
    for _ in range(N):
        data = list(map(int, input().split()))
        K = data[0]
        faces = data[1:]
        cnt = {}
        for v in faces:
            cnt[v] = cnt.get(v, 0) + 1
        dice.append((K, cnt))

    best = 0.0
    for i in range(N):
        Ki, ci = dice[i]
        # iterate j>i
        for j in range(i+1, N):
            Kj, cj = dice[j]
            # iterate over smaller dictionary
            if len(ci) <= len(cj):
                small_cnt, large_cnt = ci, cj
            else:
                small_cnt, large_cnt = cj, ci
            matching = 0
            for v, c_s in small_cnt.items():
                c_l = large_cnt.get(v)
                if c_l is not None:
                    matching += c_s * c_l
            prob = matching / (Ki * Kj)
            if prob > best:
                best = prob

    # Print with enough precision
    print("{:.15f}".format(best))


if __name__ == "__main__":
    main()