MOD = 998244353

import sys
from itertools import permutations

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        s_list = list(map(int, data[index:index+n]))
        index += n

        if n > 8:
            results.append("0")
            continue

        count_valid = 0
        for perm in permutations(range(1, n+1)):
            score = [0] * (n+1)
            black_set = set()
            valid_perm = True
            for i in range(len(perm)):
                cell = perm[i]
                if i > 0:
                    left_candidate = None
                    right_candidate = None
                    for cand in black_set:
                        if cand <= cell:
                            if left_candidate is None or cand > left_candidate:
                                left_candidate = cand
                        if cand >= cell:
                            if right_candidate is None or cand < right_candidate:
                                right_candidate = cand

                    if left_candidate is None and right_candidate is None:
                        valid_perm = False
                        break

                    if left_candidate is None:
                        chosen = right_candidate
                    elif right_candidate is None:
                        chosen = left_candidate
                    else:
                        d_left = cell - left_candidate
                        d_right = right_candidate - cell
                        if d_left < d_right:
                            chosen = left_candidate
                        elif d_left > d_right:
                            chosen = right_candidate
                        else:
                            chosen = left_candidate if left_candidate < right_candidate else right_candidate
                    score[chosen] += 1

                black_set.add(cell)

            for j in range(1, n+1):
                if s_list[j-1] != -1 and score[j] != s_list[j-1]:
                    valid_perm = False
                    break

            if valid_perm:
                count_valid = (count_valid + 1) % MOD

        results.append(str(count_valid))

    print("\n".join(results))

if __name__ == "__main__":
    main()
