def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # We want to transform A into B by flipping bits.
    # Each flip at position i changes A_i and costs sum of C_k for all k where A_k=1 after flip.

    # Key observations:
    # - Flipping a bit toggles it.
    # - We want to flip bits where A_i != B_i to fix them.
    # - The order of flips affects the cost because the cost depends on the current A after flip.
    #
    # Let's analyze the cost:
    # Initially, sumC = sum of C_i for all i where A_i=1.
    #
    # When we flip bit i:
    # - If A_i was 0, it becomes 1, so sumC increases by C_i.
    # - If A_i was 1, it becomes 0, so sumC decreases by C_i.
    #
    # The cost of the flip is the sumC after flipping.
    #
    # We want to minimize total cost = sum of costs of all flips.

    # Let's separate indices where A_i != B_i (need flip)
    need_flip = [i for i in range(N) if A[i] != B[i]]

    # If no flips needed, cost is 0
    if not need_flip:
        print(0)
        return

    # Initial sumC
    sumC = 0
    for i in range(N):
        if A[i] == 1:
            sumC += C[i]

    # We want to find the order of flipping bits in need_flip to minimize total cost.
    #
    # Each flip changes sumC by +C[i] if flipping 0->1, or -C[i] if flipping 1->0.
    #
    # Let's classify flips into two groups:
    # - flips that turn 0->1 (cost increases by C[i])
    # - flips that turn 1->0 (cost decreases by C[i])
    #
    # Flips that turn 1->0 reduce sumC, so doing them earlier reduces cost of subsequent flips.
    # Flips that turn 0->1 increase sumC, so doing them later reduces cost of subsequent flips.
    #
    # So optimal order:
    # 1) Flip all 1->0 bits first, in descending order of C[i] (flip big C[i] first to reduce sumC quickly)
    # 2) Then flip all 0->1 bits, in ascending order of C[i] (flip small C[i] first to keep sumC low longer)
    #
    # This is a greedy approach.

    flips_1_to_0 = []
    flips_0_to_1 = []

    for i in need_flip:
        if A[i] == 1 and B[i] == 0:
            flips_1_to_0.append(i)
        else:
            flips_0_to_1.append(i)

    # Sort flips_1_to_0 by descending C[i]
    flips_1_to_0.sort(key=lambda x: C[x], reverse=True)
    # Sort flips_0_to_1 by ascending C[i]
    flips_0_to_1.sort(key=lambda x: C[x])

    total_cost = 0

    # Flip 1->0 bits first
    for i in flips_1_to_0:
        # Flip bit i: sumC decreases by C[i]
        sumC -= C[i]
        total_cost += sumC

    # Flip 0->1 bits next
    for i in flips_0_to_1:
        # Flip bit i: sumC increases by C[i]
        sumC += C[i]
        total_cost += sumC

    print(total_cost)


if __name__ == "__main__":
    main()