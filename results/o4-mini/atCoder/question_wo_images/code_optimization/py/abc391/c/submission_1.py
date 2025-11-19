import sys
import threading
def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    # pigeon[i]: current nest index (0-based) of pigeon i (0-based)
    pigeon = list(range(N))
    # nest_count[j]: number of pigeons in nest j (0-based)
    nest_count = [1] * N
    multi = 0  # number of nests with count >= 2
    out = []
    for _ in range(Q):
        line = input().split()
        if line[0] == '1':
            p = int(line[1]) - 1
            h = int(line[2]) - 1
            old = pigeon[p]
            # decrement old nest
            cnt_old = nest_count[old]
            if cnt_old == 2:
                multi -= 1
            nest_count[old] = cnt_old - 1
            # increment new nest
            cnt_new = nest_count[h]
            if cnt_new == 1:
                multi += 1
            nest_count[h] = cnt_new + 1
            # update pigeon position
            pigeon[p] = h
        else:
            out.append(str(multi))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()