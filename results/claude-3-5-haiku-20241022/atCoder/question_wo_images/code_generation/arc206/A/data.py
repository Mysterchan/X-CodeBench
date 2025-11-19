n = int(input())
a = list(map(int, input().split()))

sequences = set()

for L in range(n):
    for R in range(L, n):
        # Create the sequence after operation
        new_seq = a[:L] + [a[L]] * (R - L + 1) + a[R+1:]
        sequences.add(tuple(new_seq))

print(len(sequences))