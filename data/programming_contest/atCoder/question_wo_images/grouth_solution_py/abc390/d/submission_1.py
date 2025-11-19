import sys

sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    results = set()

    def dfs(index, partitions_sum):

        if index == N:

            xor_sum = 0
            for s in partitions_sum:
                xor_sum ^= s
            results.add(xor_sum)
            return

        for i in range(len(partitions_sum)):

            partitions_sum[i] += A[index]

            dfs(index + 1, partitions_sum)

            partitions_sum[i] -= A[index]

        partitions_sum.append(A[index])

        dfs(index + 1, partitions_sum)

        partitions_sum.pop()

    dfs(0, [])

    print(len(results))

if __name__ == "__main__":
    main()