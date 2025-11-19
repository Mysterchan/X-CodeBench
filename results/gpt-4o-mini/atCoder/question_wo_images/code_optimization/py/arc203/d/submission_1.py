N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# Function to calculate the initial number of segments
def count_segments():
    segments = 0
    for i in range(N):
        if A[i] == 1:
            if i == 0 or A[i - 1] == 0:
                segments += 1
    return segments

# Count initial segments of 1s
segments = count_segments()

for _ in range(Q):
    i = int(input()) - 1
    # Flip the value at index i
    A[i] ^= 1
    
    # Update the segments count
    if A[i] == 1:  # just turned from 0 to 1
        if i == 0 or A[i - 1] == 0:  # new segment starting
            segments += 1
        if i < N - 1 and A[i + 1] == 1:  # connecting to the right segment
            segments -= 1
    else:  # just turned from 1 to 0
        if i == 0 or A[i - 1] == 1:  # breaking left segment
            segments -= 1
        if i < N - 1 and A[i + 1] == 1:  # breaking right segment
            segments -= 1
            
    # Calculate the answer based on the number of segments
    if segments == 0:
        print(2)  # All 0s
    elif segments == 1:
        print(1)  # All 1s
    else:
        print(2 + (segments - 1)*2)  # Minimum length of B is based on segments