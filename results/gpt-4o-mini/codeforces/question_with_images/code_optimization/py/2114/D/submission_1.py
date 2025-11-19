import sys

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        xs = []
        ys = []
        
        for i in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            xs.append(x)
            ys.append(y)

        if n == 1:
            results.append("1")
            continue

        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)

        A0 = (max_x - min_x + 1) * (max_y - min_y + 1)

        freq_min_x = xs.count(min_x)
        freq_max_x = xs.count(max_x)
        freq_min_y = ys.count(min_y)
        freq_max_y = ys.count(max_y)

        next_min_x = min(x for x in xs if x > min_x) if freq_min_x == 1 else min_x
        next_max_x = max(x for x in xs if x < max_x) if freq_max_x == 1 else max_x
        next_min_y = min(y for y in ys if y > min_y) if freq_min_y == 1 else min_y
        next_max_y = max(y for y in ys if y < max_y) if freq_max_y == 1 else max_y

        best_after_move = float('inf')

        for (x, y) in zip(xs, ys):
            cand_min_x = next_min_x if x == min_x else min_x
            cand_max_x = next_max_x if x == max_x else max_x
            cand_min_y = next_min_y if y == min_y else min_y
            cand_max_y = next_max_y if y == max_y else max_y

            width = cand_max_x - cand_min_x + 1
            height = cand_max_y - cand_min_y + 1
            total_cells = width * height
            
            area_i = total_cells if total_cells != n - 1 else total_cells + min(width, height)

            best_after_move = min(best_after_move, area_i)

        results.append(str(min(A0, best_after_move)))

    print("\n".join(results))

if __name__ == "__main__":
    main()