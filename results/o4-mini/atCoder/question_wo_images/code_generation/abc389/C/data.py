import sys
import threading

def main():
    import sys

    input = sys.stdin.readline

    Q = int(input())
    # We store for each snake a tuple (stored_head, length).
    # The actual head coordinate at any time is stored_head - offset.
    snakes = []
    start = 0  # index of the first (front) snake in the queue
    offset = 0  # cumulative amount subtracted from all heads due to pops

    out = []
    for _ in range(Q):
        line = input().split()
        t = int(line[0])
        if t == 1:
            l = int(line[1])
            if start == len(snakes):
                # queue was empty
                stored_head = offset
            else:
                # last snake in array is snakes[-1]
                last_head, last_len = snakes[-1]
                # new stored head = last_head + last_len
                stored_head = last_head + last_len
            snakes.append((stored_head, l))
        elif t == 2:
            # pop front
            head_len = snakes[start][1]
            offset += head_len
            start += 1
        else:  # t == 3
            k = int(line[1])
            idx = start + (k - 1)
            sh, _ = snakes[idx]
            actual = sh - offset
            out.append(str(actual))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()