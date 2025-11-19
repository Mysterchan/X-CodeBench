def determine_winner(n, m, k, tokens):
    column_count = [0] * (m + 1)
    
    for _, y in tokens:
        if y > 0:
            column_count[y] += 1
    
    total_moves = 0
    for j in range(1, m + 1):
        total_moves += column_count[j]
    
    nim_sum = 0
    for j in range(1, m + 1):
        if column_count[j] > 1:
            nim_sum ^= (column_count[j] - 1)
    
    return "Mimo" if nim_sum != 0 else "Yuyu"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m, k = map(int, data[index].split())
        index += 1
        tokens = [tuple(map(int, data[index + i].split())) for i in range(k)]
        index += k
        results.append(determine_winner(n, m, k, tokens))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()