import sys
import threading
def main():
    import sys
    from bisect import bisect_left

    input = sys.stdin.readline
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Buckets by color
    buckets = [[] for _ in range(n+1)]
    total_cost = 0
    for a, b in zip(A, B):
        buckets[b].append(a)
        total_cost += b

    answer_contrib = 0
    # For each color, compute length of LIS of its bucket
    for color in range(1, n+1):
        seq = buckets[color]
        if not seq:
            continue
        tails = []
        bl = bisect_left
        for x in seq:
            pos = bl(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        answer_contrib += color * len(tails)

    print(total_cost - answer_contrib)

if __name__ == "__main__":
    threading.Thread(target=main).start()