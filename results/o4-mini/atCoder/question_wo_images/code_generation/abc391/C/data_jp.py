import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    # nest_count[h] = number of pigeons in nest h
    nest_count = [1] * (N + 1)
    # pigeon_nest[p] = current nest of pigeon p
    pigeon_nest = list(range(N + 1))
    multi_cnt = 0

    out = []
    for _ in range(Q):
        line = input().split()
        if line[0] == '1':
            p = int(line[1])
            h = int(line[2])
            old = pigeon_nest[p]
            # Remove from old nest
            c1 = nest_count[old]
            c1_new = c1 - 1
            if c1 >= 2 and c1_new == 1:
                multi_cnt -= 1
            nest_count[old] = c1_new

            # Add to new nest
            c2 = nest_count[h]
            c2_new = c2 + 1
            if c2 == 1 and c2_new == 2:
                multi_cnt += 1
            nest_count[h] = c2_new

            # Update pigeon location
            pigeon_nest[p] = h
        else:
            # Query type 2
            out.append(str(multi_cnt))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()