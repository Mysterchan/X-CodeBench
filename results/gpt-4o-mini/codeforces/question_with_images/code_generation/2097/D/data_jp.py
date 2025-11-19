def can_transform(s, t):
    if len(s) != len(t):
        return "No"
    
    # Check if both strings have at least one '1' if they are not the same
    if s == t:
        return "Yes"
    
    # Check for presence of '1' in both s and t
    has_one_s = '1' in s
    has_one_t = '1' in t
    
    return "Yes" if has_one_s and has_one_t else "No"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        t = data[index]
        index += 1
        results.append(can_transform(s, t))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()