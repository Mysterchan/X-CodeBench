import sys
import threading

def main():
    import sys
    data = sys.stdin.readline().split()
    N = int(data[0])
    Q = int(data[1])
    # pigeon_nest[i] = current nest of pigeon i
    pigeon_nest = list(range(N+1))
    # nest_count[h] = number of pigeons in nest h
    # initialize: each nest i has pigeon i
    nest_count = [0] + [1]*N
    # number of nests with more than one pigeon
    multi = 0

    output = []
    rl = sys.stdin.readline
    for _ in range(Q):
        line = rl().split()
        if line[0] == '1':
            p = int(line[1])
            h = int(line[2])
            old_nest = pigeon_nest[p]
            # remove pigeon p from old_nest
            cnt_old_before = nest_count[old_nest]
            nest_count[old_nest] = cnt_old_before - 1
            # if it was 2 before, now 1 -> one fewer multi-occupied nest
            if cnt_old_before == 2:
                multi -= 1

            # add pigeon p to new nest h
            cnt_new_before = nest_count[h]
            nest_count[h] = cnt_new_before + 1
            # if it was 1 before, now 2 -> one more multi-occupied nest
            if cnt_new_before == 1:
                multi += 1

            # update pigeon's current nest
            pigeon_nest[p] = h
        else:
            # query type 2: report number of multi-occupied nests
            output.append(str(multi))

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()