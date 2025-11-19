import sys

def max_perfect_winners(N, M):
    # 全勝賞を与えられる選手の数は、全体の選手の数からチーム数を引いたもの
    return min(N - 1, N * M)

def main():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        results.append(max_perfect_winners(N, M))
        index += 2
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()