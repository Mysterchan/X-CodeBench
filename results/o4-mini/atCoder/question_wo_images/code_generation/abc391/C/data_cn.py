import sys
from array import array

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    # pigeon_nest[p] = current nest of pigeon p
    pigeon_nest = array('I', range(N+1))
    # nest_count[h] = number of pigeons in nest h
    # initialize all nests with 1 pigeon (index 0 unused)
    nest_count = array('I', [1]) * (N+1)
    nest_count[0] = 0

    conflict = 0  # number of nests with more than one pigeon
    outputs = []

    for _ in range(Q):
        line = input()
        if line[0] == '1':
            _, ps, hs = line.split()
            p = int(ps)
            h = int(hs)

            old_h = pigeon_nest[p]
            cnt_old = nest_count[old_h]
            if cnt_old == 2:
                conflict -= 1
            nest_count[old_h] = cnt_old - 1

            cnt_new = nest_count[h]
            if cnt_new == 1:
                conflict += 1
            nest_count[h] = cnt_new + 1

            pigeon_nest[p] = h
        else:
            # query type 2
            outputs.append(str(conflict))

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    main()