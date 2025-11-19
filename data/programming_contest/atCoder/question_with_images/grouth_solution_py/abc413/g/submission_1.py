def main():

    input = __import__('sys').stdin.readline
    H, W, K = map(int, input().split())

    block = set()
    stack = []
    for _ in range(K):
        Ri, Ci = map(int, input().split())
        if Ri == 1 or Ci == W:
            stack.append(Ri << 18 | Ci)
        else:
            block.add(Ri << 18 | Ci)

    while stack:
        x = stack.pop()
        if x >> 18 == H or x & 0x3FFFF == 1:
            print('No')
            break
        for d in (-0x40001, -0x40000, -0x3FFFF, -1, +1, +0x3FFFF, +0x40000, +0x40001):
            if (y := x + d) in block:
                block.discard(y)
                stack.append(y)
    else:
        print('Yes')

main()