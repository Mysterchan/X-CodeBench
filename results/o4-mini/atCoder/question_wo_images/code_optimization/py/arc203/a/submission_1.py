import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    res = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1])
        idx += 2
        half = m >> 1
        if m & 1:
            res.append(str(n * half + 1))
        else:
            res.append(str(n * half))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    threading.Thread(target=main).start()