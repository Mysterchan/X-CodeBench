def can_press_all_buttons_in_time(time, start_positions, goal_positions):
    from math import sqrt
    
    N = len(start_positions)
    distances = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            distances[i][j] = sqrt((start_positions[i][0] - goal_positions[j][0]) ** 2 +
                                   (start_positions[i][1] - goal_positions[j][1]) ** 2)
    
    # Create a bipartite graph where edges exist if a person can reach a button in the given time
    graph = [[] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if distances[i][j] <= time:
                graph[i].append(j)
    
    # Use DFS to find if we can match all people to buttons
    match = [-1] * N
    
    def bpm(u, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if match[v] == -1 or bpm(match[v], seen):
                    match[v] = u
                    return True
        return False
    
    # Try to find a matching for all people
    for i in range(N):
        seen = [False] * N
        bpm(i, seen)
    
    return all(m != -1 for m in match)

def min_time_to_press_buttons(start_positions, goal_positions):
    left, right = 0.0, 1e18
    answer = right
    
    while right - left > 1e-7:
        mid = (left + right) / 2
        if can_press_all_buttons_in_time(mid, start_positions, goal_positions):
            answer = mid
            right = mid
        else:
            left = mid
    
    return answer

import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
start_positions = [tuple(map(int, data[i + 1].split())) for i in range(N)]
goal_positions = [tuple(map(int, data[i + 1 + N].split())) for i in range(N)]

result = min_time_to_press_buttons(start_positions, goal_positions)
print(f"{result:.12f}")