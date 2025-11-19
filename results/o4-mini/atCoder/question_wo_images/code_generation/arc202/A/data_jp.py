import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))

        # dp: dict mapping value -> count of how many times this value can be merged up to now
        dp = dict()
        for x in A:
            if x in dp:
                # We can merge two x's into one x+1
                dp[x] -= 1
                if dp[x] == 0:
                    del dp[x]
                dp[x+1] = dp.get(x+1, 0) + 1
            else:
                dp[x] = dp.get(x, 0) + 1

        # After processing all elements, dp contains counts of values that cannot be merged further
        # The minimal number of insertions needed is sum of these counts minus 1
        # Because to get a single element, we need to merge all these remaining elements
        # We can insert elements to help merge these leftovers into one element
        total = sum(dp.values())
        print(total - 1)

if __name__ == "__main__":
    solve()