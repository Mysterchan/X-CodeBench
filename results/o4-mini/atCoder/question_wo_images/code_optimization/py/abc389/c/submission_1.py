import sys
import threading
def main():
    input = sys.stdin.readline
    Q = int(input())
    # N will store the prefix sums of snake lengths.
    # h is the index in N of the current front snake.
    N = [0, 0]
    h = 1
    total = 0
    offset = 0
    out = []
    for _ in range(Q):
        parts = input().split()
        t = parts[0]
        if t == '1':
            l = int(parts[1])
            total += l
            N.append(total)
        elif t == '2':
            # remove the front snake
            offset = N[h]
            h += 1
        else:  # t == '3'
            k = int(parts[1])
            # head coordinate = stored prefix sum minus offset of all removed lengths
            ans = N[h + k - 1] - offset
            out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()