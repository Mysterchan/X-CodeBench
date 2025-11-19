import sys
import threading

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    last_pos = {}
    best = n + 1  # INF

    for idx, value in enumerate(arr):
        if value in last_pos:
            length = idx - last_pos[value] + 1
            if length < best:
                best = length
        last_pos[value] = idx

    print(best if best <= n else -1)

if __name__ == "__main__":
    threading.Thread(target=main).start()