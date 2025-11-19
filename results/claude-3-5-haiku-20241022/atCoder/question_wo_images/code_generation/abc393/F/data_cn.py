import bisect

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    for _ in range(Q):
        R, X = map(int, input().split())
        
        # 找出前 R 個元素中,所有 <= X 的元素組成的最長嚴格遞增子序列
        lis = []
        
        for i in range(R):
            if A[i] <= X:
                # 使用二分搜尋找到插入位置
                pos = bisect.bisect_left(lis, A[i])
                if pos < len(lis):
                    lis[pos] = A[i]
                else:
                    lis.append(A[i])
        
        print(len(lis))

solve()