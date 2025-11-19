def can_transform(s, t):
    count_0_s = s.count('0')
    count_1_s = s.count('1')
    count_0_t = t.count('0')
    count_1_t = t.count('1')
    
    # To transform s to t, we must have at least one '1' in s if t has any '1' and vice versa.
    return (count_1_s > 0 and count_1_t > 0) or (count_0_s > 0 and count_0_t > 0)

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index].strip()
        index += 1
        t = data[index].strip()
        index += 1
        
        if can_transform(s, t):
            results.append('Yes')
        else:
            results.append('No')
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()