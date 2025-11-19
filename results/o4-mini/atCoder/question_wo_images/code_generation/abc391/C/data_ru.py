import sys
from array import array

def main():
    data = sys.stdin.buffer
    # Read N and Q
    first = data.readline().split()
    if not first:
        return
    N = int(first[0]); Q = int(first[1])
    # Initialize: each nest has 1 pigeon, pigeon i in nest i
    count = array('I', [1]) * (N+1)
    where = array('I', range(N+1))
    multi = 0  # number of nests with >1 pigeons

    out = []
    for _ in range(Q):
        parts = data.readline().split()
        if parts[0] == b'2':
            # Query type 2: report multi
            out.append(str(multi))
        else:
            # Query type 1: move pigeon P to nest H
            P = int(parts[1]); H = int(parts[2])
            old = where[P]
            # Remove from old nest
            c_old = count[old]
            if c_old == 2:
                multi -= 1
            count[old] = c_old - 1
            # Add to new nest
            c_new = count[H]
            if c_new == 1:
                multi += 1
            count[H] = c_new + 1
            # Update pigeon position
            where[P] = H

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()