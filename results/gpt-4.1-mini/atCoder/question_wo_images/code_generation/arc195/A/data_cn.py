import sys
import bisect

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 记录A中每个值出现的位置（升序）
    pos = {}
    for i, v in enumerate(A):
        pos.setdefault(v, []).append(i)

    # 如果B中有元素在A中不存在，直接No
    for v in B:
        if v not in pos:
            print("No")
            return

    # 从左向右匹配B，找出每个B[i]在A中最早出现的位置（严格递增）
    left_pos = [-1] * M
    current_index = -1
    for i in range(M):
        arr = pos[B[i]]
        # 找第一个大于current_index的位置
        idx = bisect.bisect_right(arr, current_index)
        if idx == len(arr):
            print("No")
            return
        current_index = arr[idx]
        left_pos[i] = current_index

    # 从右向左匹配B，找出每个B[i]在A中最晚出现的位置（严格递减）
    right_pos = [-1] * M
    current_index = N
    for i in range(M-1, -1, -1):
        arr = pos[B[i]]
        # 找第一个小于current_index的位置
        idx = bisect.bisect_left(arr, current_index) - 1
        if idx < 0:
            print("No")
            return
        current_index = arr[idx]
        right_pos[i] = current_index

    # 如果left_pos和right_pos中有任何位置left_pos[i] < right_pos[i], 说明存在两个不同子序列
    # 具体来说，存在i使得left_pos[i] < right_pos[i+1]，则可以构造两个不同子序列
    # 但更简单的判断是：如果存在i (0 <= i < M-1) 使得 left_pos[i] < right_pos[i+1]
    # 说明可以在A中找到两个不同的匹配子序列
    for i in range(M-1):
        if left_pos[i] < right_pos[i+1]:
            print("Yes")
            return

    # 如果没有上述情况，说明只有一个匹配子序列
    print("No")

if __name__ == "__main__":
    main()