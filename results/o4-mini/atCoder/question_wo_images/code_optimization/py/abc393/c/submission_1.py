import sys
import threading
def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    ans = 0
    seen = set()
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u == v:
            ans += 1
        else:
            if u > v: u, v = v, u
            key = (u << 20) | v
            if key in seen:
                ans += 1
            else:
                seen.add(key)
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    threading.Thread(target=main).start()