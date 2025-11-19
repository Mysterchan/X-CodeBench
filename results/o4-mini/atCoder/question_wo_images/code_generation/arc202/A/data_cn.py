import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        stack = []
        insertions = 0
        for x in A:
            stack.append((x,1))
            # 尝试合并
            while len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                val, cnt = stack.pop()
                val2, cnt2 = stack.pop()
                # 合并后值加1，计数为1
                new_val = val + 1
                new_cnt = 1
                # 插入合并后的元素
                stack.append((new_val, new_cnt))
        # 合并结束后，stack中元素个数即为最终长度
        # 需要插入的次数 = 最终长度 - 1
        # 因为最终要变成长度1的良好序列
        print(len(stack) - 1)

if __name__ == "__main__":
    solve()