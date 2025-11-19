def is_palindrome(s):
    return s == s[::-1]

def shortest_palindrome_path(n, edges):
    inf = float('inf')
    results = [[inf] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if edges[i][j] != '-':
                results[i][j] = 1
            if i == j:
                results[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if results[i][k] != inf and results[k][j] != inf:
                    combined_len = results[i][k] + results[k][j]
                    if combined_len < results[i][j]:
                        path_label = edges[i][k] + edges[k][j]
                        if is_palindrome(path_label):
                            results[i][j] = combined_len
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    edges = [data[i + 1] for i in range(n)]
    
    results = shortest_palindrome_path(n, edges)
    
    for i in range(n):
        for j in range(n):
            if results[i][j] == float('inf'):
                results[i][j] = -1
        print(' '.join(map(str, results[i])))

main()