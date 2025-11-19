import sys
import threading

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # N is not actually needed after reading S
    S = data[1]
    pos = []
    # Collect positions of '1'
    for i, ch in enumerate(S):
        if ch == ord('1'):
            pos.append(i)
    k = len(pos)
    # Compute median of b_i = pos[i] - i
    # Since pos is sorted and i increases, b_i is non-decreasing
    mid = pos[k // 2] - (k // 2)
    # Sum absolute differences to the median
    ans = 0
    for i, p in enumerate(pos):
        ans += abs((p - i) - mid)
    print(ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()