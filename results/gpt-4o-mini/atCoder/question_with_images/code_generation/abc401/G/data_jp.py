import sys
import math

def can_all_reach(time, start, goal):
    n = len(start)
    for j in range(n):
        reachable = False
        gx, gy = goal[j]
        for i in range(n):
            sx, sy = start[i]
            distance = math.sqrt((gx - sx) ** 2 + (gy - sy) ** 2)
            if distance <= time:
                reachable = True
                break
        if not reachable:
            return False
    return True

def find_min_time(start, goal):
    left, right = 0.0, 1e18
    while right - left > 1e-7:
        mid = (left + right) / 2
        if can_all_reach(mid, start, goal):
            right = mid
        else:
            left = mid
    return right

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    start = []
    goal = []
    
    index = 1
    for i in range(N):
        sx = int(data[index])
        sy = int(data[index + 1])
        start.append((sx, sy))
        index += 2
    
    for i in range(N):
        gx = int(data[index])
        gy = int(data[index + 1])
        goal.append((gx, gy))
        index += 2
    
    result = find_min_time(start, goal)
    print(f"{result:.12f}")

if __name__ == "__main__":
    main()