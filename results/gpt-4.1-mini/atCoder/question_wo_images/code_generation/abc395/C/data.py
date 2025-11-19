def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    last_pos = {}
    min_length = float('inf')

    for i, val in enumerate(A):
        if val in last_pos:
            # Calculate length of subarray from last occurrence to current
            length = i - last_pos[val] + 1
            if length < min_length:
                min_length = length
        last_pos[val] = i

    print(min_length if min_length != float('inf') else -1)

if __name__ == "__main__":
    main()