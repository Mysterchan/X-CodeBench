import sys
import threading

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    snakes = [tuple(map(int, input().split())) for _ in range(N)]
    base = [t * l for t, l in snakes]
    for k in range(1, D + 1):
        max_w = 0
        for (t, _), b in zip(snakes, base):
            w = b + t * k
            if w > max_w:
                max_w = w
        sys.stdout.write(str(max_w) + "\n")

if __name__ == "__main__":
    threading.Thread(target=main).start()