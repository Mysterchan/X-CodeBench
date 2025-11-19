def count_intersections(N, M, lines):
    # To store the number of intersections
    intersection_count = 0
    
    # Create a list to store the lines
    segments = []
    
    for a, b in lines:
        # Ensure a < b for consistency
        if a > b:
            a, b = b, a
        segments.append((a, b))
    
    # Sort segments based on the first point, and then by the second point
    segments.sort()
    
    # Use a sweep line approach with a sorted list of endpoints
    from sortedcontainers import SortedList
    
    active_segments = SortedList()
    
    for i in range(M):
        a, b = segments[i]
        
        # Count how many segments in active_segments intersect with the current segment
        # An intersection occurs if there exists a segment (c, d) such that:
        # (c < a < d) and (c < b < d) or (a < c < b) and (a < d < b)
        # This can be simplified to checking the active segments
        # We need to find the number of segments that intersect with (a, b)
        
        # Count segments that start before b and end after a
        left_count = active_segments.bisect_right(b)  # count of segments that end before or at b
        right_count = active_segments.bisect_left(a)  # count of segments that start after or at a
        
        # The number of intersecting segments is the difference
        intersection_count += (left_count - right_count)
        
        # Add the current segment to the active segments
        active_segments.add((a, b))
    
    return intersection_count

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
lines = [tuple(map(int, line.split())) for line in data[1:M+1]]

# Get the result
result = count_intersections(N, M, lines)

# Print the result
print(result)