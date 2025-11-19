import sys

input = sys.stdin.read
data = input().splitlines()

def can_reach_terminal_point(t, test_cases):
    results = []
    index = 0
    for _ in range(t):
        n = test_cases[index]
        p_x, p_y, q_x, q_y = test_cases[index + 1]
        moves = test_cases[index + 2]
        index += 3
        
        distance_to_terminal = abs(q_x - p_x) + abs(q_y - p_y)
        total_distance_possible = sum(moves)

        if distance_to_terminal <= total_distance_possible and (total_distance_possible - distance_to_terminal) % 2 == 0:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

if __name__ == "__main__":
    t = int(data[0])
    test_cases = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        coordinates = tuple(map(int, data[index + 1].split()))
        moves = list(map(int, data[index + 2].split()))
        test_cases.append(n)
        test_cases.append(coordinates)
        test_cases.append(moves)
        index += 3
    results = can_reach_terminal_point(t, test_cases)
    print("\n".join(results))