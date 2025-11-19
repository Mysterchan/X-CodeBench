import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        if n - 1 > 0:
            parents = list(map(int, data[index:index+n-1]))
            index += n - 1
        else:
            parents = []
            index += 0
        
        children = [[] for _ in range(n+1)]
        for i in range(2, n+1):
            p = parents[i-2]
            children[p].append(i)
        
        matches = [0] * (n+1)
        excess = [0] * (n+1)
        
        for u in range(n, 0, -1):
            if not children[u]:
                excess[u] = 1
            else:
                S = 0
                M = 0
                total_matches = 0
                for v in children[u]:
                    S += excess[v]
                    if excess[v] > M:
                        M = excess[v]
                    total_matches += matches[v]
                pairs = min(S // 2, S - M)
                matches[u] = total_matches + pairs
                excess[u] = 1 + (S - 2 * pairs)
                
        results.append(str(matches[1]))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()