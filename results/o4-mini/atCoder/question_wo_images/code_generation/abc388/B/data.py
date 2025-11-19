import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    D = int(next(it))

    # Precompute base weights and thicknesses
    base_weights = []
    thicknesses = []
    for _ in range(N):
        t = int(next(it))
        l = int(next(it))
        base_weights.append(t * l)
        thicknesses.append(t)

    # For each k from 1 to D, compute the maximum weight
    output = []
    for k in range(1, D + 1):
        max_weight = max(base_weights[i] + thicknesses[i] * k for i in range(N))
        output.append(str(max_weight))

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()