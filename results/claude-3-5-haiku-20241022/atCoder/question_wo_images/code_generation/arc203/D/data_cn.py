def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    
    def count_segments(arr):
        if not arr:
            return 0
        count = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                count += 1
        return count
    
    for _ in range(Q):
        i = int(input())
        A[i-1] = 1 - A[i-1]
        
        # Find first and last 1
        first_one = -1
        last_one = -1
        for j in range(N):
            if A[j] == 1:
                if first_one == -1:
                    first_one = j
                last_one = j
        
        if first_one == -1:
            # All zeros
            print(N)
        else:
            # Count segments in the range [first_one, last_one]
            segments = count_segments(A[first_one:last_one+1])
            print(segments)

solve()