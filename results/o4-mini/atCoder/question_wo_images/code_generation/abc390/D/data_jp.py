import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    # block_sums[b] = sum of A[i] assigned to block b
    block_sums = [0] * N
    result = set()

    def dfs(idx, blocks):
        if idx == N:
            # compute XOR of all non-empty blocks
            x = 0
            for i in range(blocks):
                x ^= block_sums[i]
            result.add(x)
            return
        ai = A[idx]
        # try adding A[idx] to each existing block
        for b in range(blocks):
            prev = block_sums[b]
            block_sums[b] = prev + ai
            dfs(idx + 1, blocks)
            block_sums[b] = prev
        # try creating a new block with A[idx]
        block_sums[blocks] = ai
        dfs(idx + 1, blocks + 1)
        block_sums[blocks] = 0

    dfs(0, 0)
    print(len(result))

if __name__ == "__main__":
    main()