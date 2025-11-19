def max_triangle_score(n, m, a, b):
    k_max = min(n, m)
    scores = []
    
    for k in range(1, k_max + 1):
        score = 0
        # Calculate the maximum score for k operations
        score += k * (max(a) - min(a)) * 2
        scores.append(score)
        
        # Remove the used points
        a = a[1:]  # Remove the leftmost point
        b = b[1:]  # Remove the leftmost point
    
    return k_max, scores

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        a = list(map(int, data[index + 1].split()))
        b = list(map(int, data[index + 2].split()))
        index += 3
        
        k_max, scores = max_triangle_score(n, m, a, b)
        results.append(f"{k_max}")
        if k_max > 0:
            results.append(" ".join(map(str, scores)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()