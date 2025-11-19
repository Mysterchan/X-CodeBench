import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    
    N = int(input())
    contests = []
    for _ in range(N):
        L, R = map(int, input().split())
        contests.append((L, R))
    
    # すべてのレーティング変化ポイントを収集
    events = set()
    for L, R in contests:
        events.add(L)
        events.add(R + 1)
    
    # ソートして、各区間での増加数を計算
    points = sorted(events)
    
    # 各ポイントでの累積増加数を計算
    cumulative = [0]
    for i in range(len(points) - 1):
        rating = points[i]
        increase = 0
        for L, R in contests:
            if L <= rating <= R:
                increase += 1
        cumulative.append(cumulative[-1] + increase)
    
    Q = int(input())
    for _ in range(Q):
        X = int(input())
        
        # Xがどの区間に属するか
        idx = bisect_left(points, X)
        if idx < len(points) and points[idx] == X:
            # Xがポイントと一致
            current_rating = X
            total_increase = 0
            
            for i in range(len(points)):
                if i >= idx:
                    rating_at_start = current_rating
                    # この区間での増加数を計算
                    increase = 0
                    for L, R in contests:
                        if L <= rating_at_start <= R:
                            increase += 1
                    
                    if i == len(points) - 1:
                        total_increase += increase
                        break
                    
                    # 次のポイントまで到達するか確認
                    next_point = points[i + 1]
                    if rating_at_start + increase >= next_point:
                        # 次の区間に到達
                        steps_to_next = next_point - rating_at_start
                        total_increase += steps_to_next
                        current_rating = next_point
                    else:
                        # この区間で終了
                        total_increase += increase
                        break
            
            print(X + total_increase)
        else:
            # Xがポイント間にある
            current_rating = X
            total_increase = 0
            
            for i in range(idx, len(points)):
                rating_at_start = current_rating
                increase = 0
                for L, R in contests:
                    if L <= rating_at_start <= R:
                        increase += 1
                
                if i == len(points) - 1:
                    total_increase += increase
                    break
                
                next_point = points[i + 1] if i + 1 < len(points) else float('inf')
                if rating_at_start + increase >= next_point:
                    steps_to_next = next_point - rating_at_start
                    total_increase += steps_to_next
                    current_rating = next_point
                else:
                    total_increase += increase
                    break
            
            print(X + total_increase)

if __name__ == "__main__":
    main()