import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    Q = int(input())
    # S[i] will be the prefix sum of lengths up to the i-th added snake (0-based),
    # with S[0] = 0.
    S = [0]
    head = 0  # how many snakes have been removed from the front
    out = []
    for _ in range(Q):
        parts = input().split()
        t = parts[0]
        if t == '1':
            l = int(parts[1])
            S.append(S[-1] + l)
        elif t == '2':
            # remove the first snake
            head += 1
        else:  # t == '3'
            k = int(parts[1])
            idx = head + k - 1
            # head-position = sum of lengths before this snake in the current queue
            ans = S[idx] - S[head]
            out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()