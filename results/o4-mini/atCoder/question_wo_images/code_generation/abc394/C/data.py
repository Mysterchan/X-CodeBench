import sys
import heapq

def main():
    S = list(sys.stdin.readline().rstrip("\n"))
    n = len(S)
    if n < 2:
        # No possible "WA" in strings shorter than 2
        print("".join(S))
        return

    # presentWA[i] is True if S[i:i+2] == "WA"
    presentWA = [False] * (n - 1)
    heap = []

    # Initialize the heap with all starting positions of "WA"
    for i in range(n - 1):
        if S[i] == 'W' and S[i + 1] == 'A':
            presentWA[i] = True
            heapq.heappush(heap, i)

    # Process replacements: always replace the leftmost "WA"
    while True:
        # Pop stale entries
        while heap and not presentWA[heap[0]]:
            heapq.heappop(heap)
        if not heap:
            break

        i = heapq.heappop(heap)
        # Mark this WA as consumed
        presentWA[i] = False

        # Perform the replacement WA -> AC
        S[i], S[i + 1] = 'A', 'C'

        # After changing S at i, i+1, "WA" occurrences might change at i-1, i, i+1
        for j in (i - 1, i, i + 1):
            if 0 <= j < n - 1:
                is_now_WA = (S[j] == 'W' and S[j + 1] == 'A')
                if is_now_WA and not presentWA[j]:
                    # New WA formed: add it
                    presentWA[j] = True
                    heapq.heappush(heap, j)
                elif (not is_now_WA) and presentWA[j]:
                    # Existing WA destroyed: mark false
                    presentWA[j] = False

    # Output final string
    print("".join(S))

if __name__ == "__main__":
    main()