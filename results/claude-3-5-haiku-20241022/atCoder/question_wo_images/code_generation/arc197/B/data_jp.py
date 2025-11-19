def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    max_score = 0
    
    # すべての可能な部分列を試す
    for mask in range(1, 1 << N):
        subsequence = []
        for i in range(N):
            if mask & (1 << i):
                subsequence.append(A[i])
        
        # 平均値を計算
        avg = sum(subsequence) / len(subsequence)
        
        # スコアを計算
        score = sum(1 for x in subsequence if x > avg)
        
        max_score = max(max_score, score)
    
    return max_score

T = int(input())
for _ in range(T):
    print(solve())