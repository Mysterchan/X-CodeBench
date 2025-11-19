import sys
import threading

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    last_pos = {}
    ans = N + 1

    for i, x in enumerate(A):
        if x in last_pos:
            length = i - last_pos[x] + 1
            if length < ans:
                ans = length
        last_pos[x] = i

    print(ans if ans <= N else -1)

if __name__ == "__main__":
    threading.Thread(target=main).start()