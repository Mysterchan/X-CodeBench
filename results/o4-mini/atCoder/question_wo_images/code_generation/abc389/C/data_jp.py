import sys
import threading
def main():
    import sys
    input = sys.stdin.readline

    Q = int(input())
    pos_list = []
    len_list = []
    head = 0
    D = 0
    out = []

    for _ in range(Q):
        line = input().split()
        t = int(line[0])
        if t == 1:
            l = int(line[1])
            if head == len(pos_list):
                # queue is empty
                pos = -D
            else:
                # extend after the last snake
                pos = pos_list[-1] + len_list[-1]
            pos_list.append(pos)
            len_list.append(l)
        elif t == 2:
            # pop front
            m = len_list[head]
            head += 1
            D -= m
        else:  # t == 3
            k = int(line[1])
            idx = head + k - 1
            out.append(str(pos_list[idx] + D))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()