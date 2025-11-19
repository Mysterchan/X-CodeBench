def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # If there are no zeros, answer is Yes immediately
    if all(x == 1 for x in A):
        print("Yes")
        return

    # The operations allow us to set A_i and A_{i+1} to 1 if the substring of S at positions
    # (i, i+1, i+2) (mod N) is either "ARC" or "CRA" (circularly).
    #
    # We want to know if there exists a string S of length N over uppercase letters such that
    # by applying these operations any number of times, all zeros in A can be turned into ones.
    #
    # Key insight:
    # Each operation can fix two adjacent positions i and i+1 if the triple at (i, i+1, i+2) is "ARC"
    # or the triple at (i, i+1, i+2) reversed is "CRA".
    #
    # Since the string S is arbitrary, we can choose S to facilitate fixing zeros.
    #
    # Let's analyze the problem:
    #
    # - Each operation fixes two adjacent positions.
    # - The triple pattern is either "ARC" or "CRA" (in circular order).
    #
    # We want to cover all zeros in A with pairs (i, i+1) that can be fixed by some triple in S.
    #
    # Since S is arbitrary, we can assign letters to make any triple "ARC" or "CRA" at any position.
    #
    # So the problem reduces to:
    # Can we cover all zeros in A by pairs of adjacent indices (i, i+1) (mod N)?
    #
    # Because each operation fixes A_i and A_{i+1} simultaneously.
    #
    # So, if the zeros in A can be covered by pairs of adjacent indices (mod N), then answer is Yes.
    #
    # Otherwise, No.
    #
    # This means:
    # - If there is an isolated zero (a zero that is not adjacent to any other zero), it cannot be fixed.
    # - Because operation fixes pairs of adjacent positions.
    #
    # So the problem reduces to checking if the zeros in A can be partitioned into pairs of adjacent zeros.
    #
    # Since the string is circular, adjacency is modulo N.
    #
    # Let's find all zero positions and check if they can be paired up with adjacent zeros.
    #
    # Approach:
    # - Find all zero positions.
    # - Group zeros into connected segments of zeros (consecutive zeros in circular manner).
    # - For each segment, check if the length of the segment is even.
    #   Because each operation fixes two adjacent zeros at once.
    #
    # If all zero segments have even length, answer is Yes.
    # Otherwise, No.

    # Find zero segments in circular array
    zero_positions = [i for i, val in enumerate(A) if val == 0]
    if not zero_positions:
        print("Yes")
        return

    # To handle circular segments, we check if zeros wrap around from end to start
    # We'll find segments of consecutive zeros in circular manner

    # Mark zeros in a boolean array for convenience
    zero_mask = [val == 0 for val in A]

    segments = []
    visited = [False] * N

    for i in range(N):
        if zero_mask[i] and not visited[i]:
            # Start a new segment
            length = 0
            pos = i
            while zero_mask[pos] and not visited[pos]:
                visited[pos] = True
                length += 1
                pos = (pos + 1) % N
            segments.append(length)

    # Check if all segments have even length
    for seg_len in segments:
        if seg_len % 2 != 0:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()