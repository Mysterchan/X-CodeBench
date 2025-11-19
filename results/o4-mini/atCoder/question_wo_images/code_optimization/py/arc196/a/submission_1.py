import sys
import threading
def main():
    import sys
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    A = list(map(int, data[1:]))
    A.sort()
    l, r = 0, n - 1
    ans = 0
    while l < r:
        ans += A[r] - A[l]
        l += 1
        r -= 1
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    threading.Thread(target=main).start()