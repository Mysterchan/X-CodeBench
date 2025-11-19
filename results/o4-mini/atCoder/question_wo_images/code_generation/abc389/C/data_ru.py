import sys
import threading

def main():
    import sys
    data = sys.stdin
    Q = int(data.readline())
    head = [0] * Q
    length = [0] * Q
    front = 0
    back = 0
    shift = 0
    out = []

    for _ in range(Q):
        parts = data.readline().split()
        t = parts[0]
        if t == '1':
            l = int(parts[1])
            if back == front:
                # queue was empty
                h = shift
            else:
                # last stored head and length
                h = head[back - 1] + length[back - 1]
            head[back] = h
            length[back] = l
            back += 1
        elif t == '2':
            # pop front
            m = length[front]
            front += 1
            shift += m
        else:  # t == '3'
            k = int(parts[1])
            idx = front + k - 1
            ans = head[idx] - shift
            out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()