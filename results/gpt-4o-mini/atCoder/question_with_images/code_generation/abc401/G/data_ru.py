def can_all_reach_in_time(people, buttons, time):
    from collections import deque
    
    N = len(people)
    graph = [[] for _ in range(N)]
    
    for i in range(N):
        sx, sy = people[i]
        for j in range(N):
            gx, gy = buttons[j]
            distance = ((sx - gx) ** 2 + (sy - gy) ** 2) ** 0.5
            if distance <= time:
                graph[i].append(j)
    
    def bpm():
        match = [-1] * N
        def try_match(u, visited):
            for v in graph[u]:
                if visited[v]:
                    continue
                visited[v] = True
                if match[v] == -1 or try_match(match[v], visited):
                    match[v] = u
                    return True
            return False
        
        matches = 0
        for u in range(N):
            visited = [False] * N
            if try_match(u, visited):
                matches += 1
        return matches == N
    
    return bpm()

def min_time_to_reach(people, buttons):
    left, right = 0.0, 1e18
    while right - left > 1e-7:
        mid = (left + right) / 2
        if can_all_reach_in_time(people, buttons, mid):
            right = mid
        else:
            left = mid
    return right

import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
people = [tuple(map(int, data[i + 1].split())) for i in range(N)]
buttons = [tuple(map(int, data[i + 1 + N].split())) for i in range(N)]

result = min_time_to_reach(people, buttons)
print(f"{result:.10f}")