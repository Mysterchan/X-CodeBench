import sys
import heapq

def main():
    S = list(sys.stdin.readline().strip())
    n = len(S)
    heap = []
    for i in range(n - 1):
        if S[i] == 'W' and S[i + 1] == 'A':
            heapq.heappush(heap, i)
    while heap:
        i = heapq.heappop(heap)
        if i < 0 or i >= n - 1:
            continue
        if S[i] == 'W' and S[i + 1] == 'A':
            S[i], S[i + 1] = 'A', 'C'
            for j in (i - 1, i, i + 1):
                if 0 <= j < n - 1 and S[j] == 'W' and S[j + 1] == 'A':
                    heapq.heappush(heap, j)
    sys.stdout.write(''.join(S))

if __name__ == '__main__':
    main()