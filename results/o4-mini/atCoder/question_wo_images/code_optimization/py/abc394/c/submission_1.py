import sys
import threading

def main():
    import sys
    data = sys.stdin.readline().rstrip()
    n = len(data)
    s = list(data)

    # Min-heap to keep track of starting indices of "WA"
    import heapq
    heap = []
    for i in range(n - 1):
        if s[i] == 'W' and s[i + 1] == 'A':
            heap.append(i)
    heapq.heapify(heap)

    # Process replacements
    while heap:
        i = heapq.heappop(heap)
        # Skip if this "WA" has already been destroyed
        if not (s[i] == 'W' and s[i + 1] == 'A'):
            continue

        # Replace WA -> AC
        s[i], s[i + 1] = 'A', 'C'

        # Only position i-1 could form a new "WA"
        j = i - 1
        if j >= 0 and s[j] == 'W' and s[j + 1] == 'A':
            heapq.heappush(heap, j)

    sys.stdout.write(''.join(s))

if __name__ == "__main__":
    main()