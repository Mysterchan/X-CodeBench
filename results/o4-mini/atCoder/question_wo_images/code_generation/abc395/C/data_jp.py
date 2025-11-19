import sys
import threading
def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    last = {}
    ans = N + 1
    for j, v in enumerate(A):
        if v in last:
            length = j - last[v] + 1
            if length < ans:
                ans = length
        last[v] = j
    if ans == N + 1:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()