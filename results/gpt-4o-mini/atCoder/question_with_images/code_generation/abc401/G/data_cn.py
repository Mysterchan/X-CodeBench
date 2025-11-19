def can_all_reach_in_time(people, buttons, time):
    n = len(people)
    for i in range(n):
        reachable = False
        for j in range(n):
            distance = ((people[i][0] - buttons[j][0]) ** 2 + (people[i][1] - buttons[j][1]) ** 2) ** 0.5
            if distance <= time:
                reachable = True
                break
        if not reachable:
            return False
    return True

def min_time_to_reach(people, buttons):
    left, right = 0.0, 1e18
    while right - left > 1e-7:
        mid = (left + right) / 2
        if can_all_reach_in_time(people, buttons, mid):
            right = mid
        else:
            left = mid
    return right

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    people = [tuple(map(int, data[i + 1].split())) for i in range(N)]
    buttons = [tuple(map(int, data[i + 1 + N].split())) for i in range(N)]
    
    result = min_time_to_reach(people, buttons)
    print(f"{result:.10f}")

if __name__ == "__main__":
    main()