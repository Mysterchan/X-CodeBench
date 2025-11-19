def duel_turns(n, m, a, b):
    # Calculate the number of turns based on the position of the monster
    top = a - 1
    bottom = n - a
    left = b - 1
    right = m - b
    
    # The number of turns is determined by the minimum of the maximum possible cuts
    return min(max(top, bottom), max(left, right)) + 1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, m, a, b = map(int, data[i].split())
        results.append(duel_turns(n, m, a, b))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()