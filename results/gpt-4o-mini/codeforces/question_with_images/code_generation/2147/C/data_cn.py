def can_place_rabbits(n, s):
    # Find the leftmost and rightmost empty pots
    leftmost_empty = s.find('0')
    rightmost_empty = s.rfind('0')
    
    # If there are no empty pots or they are adjacent, return 'YES'
    if leftmost_empty == -1 or (leftmost_empty == rightmost_empty):
        return "YES"
    
    # Check if any filled pot is directly next to empty pots
    for i in range(leftmost_empty, rightmost_empty):
        if s[i] == '1' and (s[i+1] == '0' or (i > 0 and s[i-1] == '0')):
            return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])  # Number of test cases
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])  # Size of the current case
        s = data[index + 1]   # Binary string representing pots
        results.append(can_place_rabbits(n, s))
        index += 2
    
    print("\n".join(results))

if __name__ == "__main__":
    main()