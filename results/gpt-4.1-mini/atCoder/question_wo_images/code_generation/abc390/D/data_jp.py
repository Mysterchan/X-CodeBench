def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # 袋の石の個数の集合の XOR の値としてあり得るものは、
    # 操作により袋の石を他の袋にすべて移すことができるため、
    # 袋の石の個数の集合は、元の石の個数の集合の線形結合（XOR和）で表される。
    #
    # つまり、Aの要素の部分集合のXOR和としてあり得る値の集合が求める集合となる。
    #
    # したがって、Aの部分集合のXOR和の個数を求めればよい。
    #
    # N <= 12 なので、2^N = 4096 で全探索可能。

    possible = {0}
    for a in A:
        new_possible = set(possible)
        for x in possible:
            new_possible.add(x ^ a)
        possible = new_possible

    print(len(possible))


if __name__ == "__main__":
    main()