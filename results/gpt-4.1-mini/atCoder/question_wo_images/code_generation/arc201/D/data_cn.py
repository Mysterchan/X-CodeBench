import sys
import bisect

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B_sorted = sorted(B)

    # 对于每个 B_i，寻找 A_j 使得 (A_j + B_i) % M 尽可能小
    # 目标是最小化 max((A_j + B_i) % M)
    # 思路：对每个 B_i，寻找 A_j >= (M - B_i) % M 的最小元素，若无则取最小的 A_j
    # 这样 (A_j + B_i) % M 会尽量小

    # 由于要最小化最大值，直接贪心匹配即可
    # 具体实现：
    # 对 B_sorted 中每个 b，寻找 A 中第一个 >= (M - b) % M 的元素
    # 如果找不到，取 A 中最小元素
    # 计算 (a + b) % M，记录最大值

    res = 0
    for b in B_sorted:
        target = (M - b) % M
        idx = bisect.bisect_left(A, target)
        if idx == len(A):
            idx = 0
        val = (A[idx] + b) % M
        if val > res:
            res = val
        A.pop(idx)  # 移除已用元素

    print(res)