import sys
import threading

def main():
    import sys

    data = sys.stdin
    N_line = data.readline()
    while N_line.strip() == "":
        N_line = data.readline()
    N = int(N_line)
    Ks = [0] * N
    counts = [None] * N
    for i in range(N):
        parts = data.readline().split()
        while not parts:
            parts = data.readline().split()
        k = int(parts[0])
        Ks[i] = k
        cnt = {}
        for x in parts[1:]:
            v = int(x)
            cnt[v] = cnt.get(v, 0) + 1
        # In case the line was split, read remaining values
        read = len(parts) - 1
        while read < k:
            parts = data.readline().split()
            for x in parts:
                v = int(x)
                cnt[v] = cnt.get(v, 0) + 1
            read += len(parts)
        counts[i] = cnt

    # Pre-store items lists to avoid repeated .items() calls
    items_list = [list(cnt.items()) for cnt in counts]

    max_num = 0
    max_den = 1

    for i in range(N):
        Ki = Ks[i]
        ci_items = items_list[i]
        size_i = len(ci_items)
        for j in range(i + 1, N):
            Kj = Ks[j]
            den = Ki * Kj
            cj = counts[j]
            # iterate over the smaller dictionary
            if size_i <= len(cj):
                num = 0
                for v, ci_v in ci_items:
                    cj_v = cj.get(v)
                    if cj_v is not None:
                        num += ci_v * cj_v
            else:
                num = 0
                for v, cj_v in items_list[j]:
                    ci_v = counts[i].get(v)
                    if ci_v is not None:
                        num += ci_v * cj_v

            # Compare num/den with current max_num/max_den via cross-multiplication
            if num * max_den > max_num * den:
                max_num = num
                max_den = den

    # Compute final answer
    ans = 0.0
    if max_num != 0:
        ans = max_num / max_den

    # Print with sufficient precision
    print("{:.15f}".format(ans))

if __name__ == "__main__":
    main()