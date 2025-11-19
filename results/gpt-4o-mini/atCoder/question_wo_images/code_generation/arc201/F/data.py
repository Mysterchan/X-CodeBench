import sys
input = sys.stdin.read

def max_contests(writers):
    div1 = div2 = div3 = 0
    results = []

    # Iterate over each writer's proposals
    for writer in writers:
        a, b, c, d, e = writer
        # Calculate possible contests for each division
        div1 += min(a, b, c)
        div2 += min(b, c, d)
        div3 += min(c, d, e)
        # The maximum number of contests that can be held with k writers
        results.append(max(div1, div2, div3))

    return results

def main():
    data = input().splitlines()
    index = 0
    T = int(data[index])
    index += 1
    results_list = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        writers = []
        for __ in range(N):
            writers.append(tuple(map(int, data[index].split())))
            index += 1
        results = max_contests(writers)
        results_list.append(" ".join(map(str, results)))

    # Print all results for each test case
    print("\n".join(results_list))

if __name__ == "__main__":
    main()