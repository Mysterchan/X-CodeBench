import sys
input = sys.stdin.readline

def main():
    N, M, A, B = map(int, input().split())
    bad_intervals = [tuple(map(int, input().split())) for _ in range(M)]

    # 合法区间是 [1, N] 除去坏区间
    # 先构造所有合法区间（非坏区间）
    good_intervals = []
    prev_end = 0
    for L, R in bad_intervals:
        if prev_end + 1 <= L - 1:
            good_intervals.append([prev_end + 1, L - 1])
        prev_end = R
    if prev_end < N:
        good_intervals.append([prev_end + 1, N])

    # 起点1必定是合法区间的起点之一，否则直接No
    # 维护当前可达区间集合，初始为包含1的区间的起点1
    # 通过滑动窗口思想，模拟跳跃范围[A,B]，判断能否到达N

    # 当前可达区间集合，存储为非重叠区间列表
    # 初始可达区间为包含1的区间的起点1
    # 找包含1的区间
    start_intervals = []
    for s,e in good_intervals:
        if s <= 1 <= e:
            start_intervals.append([1,1])
            break
    else:
        # 1是坏块，无法开始
        print("No")
        return

    # 维护可达区间列表，初始为[1,1]
    reachable = [[1,1]]

    # good_intervals是合法区间，且不重叠且有序
    # 我们用双指针遍历good_intervals和reachable，模拟跳跃
    # 对于当前reachable区间[r_s, r_e]，跳跃范围是[r_s + A, r_e + B]
    # 在good_intervals中找到与该跳跃范围相交的区间，加入新的reachable区间
    # 合并所有新reachable区间，直到不再扩展或覆盖N

    gi_idx = 0  # good_intervals索引
    while True:
        new_reachable = []
        # 计算所有reachable区间跳跃后可达区间的并集
        # 先合并reachable区间，保证不重叠
        merged_reach = []
        for s,e in reachable:
            if not merged_reach:
                merged_reach.append([s,e])
            else:
                if s <= merged_reach[-1][1] + 1:
                    merged_reach[-1][1] = max(merged_reach[-1][1], e)
                else:
                    merged_reach.append([s,e])
        reachable = merged_reach

        # 对每个reachable区间，计算跳跃后区间
        jump_intervals = []
        for s,e in reachable:
            jump_intervals.append([s + A, e + B])
        # 合并jump_intervals
        jump_intervals.sort()
        merged_jump = []
        for s,e in jump_intervals:
            if e > N:
                e = N
            if s > N:
                continue
            if not merged_jump:
                merged_jump.append([s,e])
            else:
                if s <= merged_jump[-1][1] + 1:
                    merged_jump[-1][1] = max(merged_jump[-1][1], e)
                else:
                    merged_jump.append([s,e])

        # 在good_intervals中找与merged_jump相交的部分，作为新的reachable
        new_reachable = []
        gi_ptr = 0
        for js, je in merged_jump:
            # 移动gi_ptr到good_intervals中第一个end >= js的区间
            while gi_ptr < len(good_intervals) and good_intervals[gi_ptr][1] < js:
                gi_ptr += 1
            idx = gi_ptr
            while idx < len(good_intervals) and good_intervals[idx][0] <= je:
                # 计算交集
                inter_s = max(js, good_intervals[idx][0])
                inter_e = min(je, good_intervals[idx][1])
                if inter_s <= inter_e:
                    if not new_reachable:
                        new_reachable.append([inter_s, inter_e])
                    else:
                        if inter_s <= new_reachable[-1][1] + 1:
                            new_reachable[-1][1] = max(new_reachable[-1][1], inter_e)
                        else:
                            new_reachable.append([inter_s, inter_e])
                idx += 1

        if not new_reachable:
            # 无法前进
            print("No")
            return

        # 如果新reachable包含N，成功
        if new_reachable[-1][1] >= N:
            print("Yes")
            return

        # 如果新reachable与旧reachable相同，说明无法继续扩展，失败
        if new_reachable == reachable:
            print("No")
            return

        reachable = new_reachable

if __name__ == "__main__":
    main()