def can_transform(N, X, Y, S, T):
    # Count the number of 0s and 1s in S and T
    count_S = [0, 0]
    count_T = [0, 0]
    
    for char in S:
        count_S[int(char)] += 1
    for char in T:
        count_T[int(char)] += 1
    
    # Check if the total number of 0s and 1s can match
    if count_S[0] < count_T[0] or count_S[1] < count_T[1]:
        return "No"
    
    # Check the segments of 0s and 1s
    zero_segments_S = []
    one_segments_S = []
    
    i = 0
    while i < N:
        if S[i] == '0':
            start = i
            while i < N and S[i] == '0':
                i += 1
            zero_segments_S.append(i - start)
        else:
            start = i
            while i < N and S[i] == '1':
                i += 1
            one_segments_S.append(i - start)
    
    zero_segments_T = []
    one_segments_T = []
    
    i = 0
    while i < N:
        if T[i] == '0':
            start = i
            while i < N and T[i] == '0':
                i += 1
            zero_segments_T.append(i - start)
        else:
            start = i
            while i < N and T[i] == '1':
                i += 1
            one_segments_T.append(i - start)
    
    # Check if we can match the segments
    def can_match_segments(segments_S, segments_T, X, Y):
        total_S = sum(segments_S)
        total_T = sum(segments_T)
        
        if total_S < total_T:
            return False
        
        # We can only change segments of size X and Y
        for seg in segments_S:
            if seg >= X:
                total_S -= X
                total_T -= 1
            if seg >= Y:
                total_S -= Y
                total_T -= 1
        
        return total_T <= 0
    
    if can_match_segments(zero_segments_S, zero_segments_T, X, Y) and can_match_segments(one_segments_S, one_segments_T, Y, X):
        return "Yes"
    
    return "No"

# Read input
N, X, Y = map(int, input().split())
S = input().strip()
T = input().strip()

# Output the result
print(can_transform(N, X, Y, S, T))