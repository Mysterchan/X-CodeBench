import sys


def canonical(bit_string, block_len, num_blocks):
    if block_len == 1:
        return (1,) if '1' in bit_string else ()
    basis = {}
    idx = 0
    for _ in range(num_blocks):
        block = bit_string[idx:idx + block_len]
        idx += block_len
        val = int(block, 2)
        x = val
        while x:
            pivot = x.bit_length() - 1
            current = basis.get(pivot)
            if current is None:
                basis[pivot] = x
                break
            x ^= current
    if not basis:
        return ()
    pivots = sorted(basis.keys(), reverse=True)
    vectors = [basis[p] for p in pivots]
    for pos in range(len(vectors) - 1, -1, -1):
        pivot = pivots[pos]
        vec = vectors[pos]
        for j in range(pos):
            if (vectors[j] >> pivot) & 1:
                vectors[j] ^= vec
    return tuple(vectors)


def solve():
    input = sys.stdin.readline
    t = int(input())
    answers = []
    for _ in range(t):
        n = int(input())
        s = input().strip()
        target = input().strip()
        tmp = n
        shift = 0
        while tmp % 2 == 0:
            tmp //= 2
            shift += 1
        block_len = tmp
        num_blocks = 1 << shift
        if num_blocks == 1:
            answers.append("Yes" if s == target else "No")
            continue
        canon_s = canonical(s, block_len, num_blocks)
        canon_t = canonical(target, block_len, num_blocks)
        answers.append("Yes" if canon_s == canon_t else "No")
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()
