N = int(input())
A = list(map(int, input().split()))
def xor_basis(arr):
  basis = []
  for x in arr:
    for b in basis:
      x = min(x, x ^ b)
    if x > 0:
      basis.append(x)
  return basis
basis = xor_basis(A)
print(2 ** len(basis))