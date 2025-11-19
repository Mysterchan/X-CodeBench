n, k = map(int, input().split())
k = (k - 1) % (2 * n - 2) + 1
mat = [[0] * n for _ in range(n)]
def path(i=0, j=0):
  if i + 1 < n and j + 1 < n:
    if mat[i + 1][j] > mat[i][j + 1]:
      mat[i][j + 1] += 1
      path(i, j + 1)
    else:
      mat[i + 1][j] += 1
      path(i + 1, j)
  elif i + 1 < n:
    mat[i + 1][j] += 1
    path(i + 1, j)
  elif j + 1 < n:
    mat[i][j + 1] += 1
    path(i, j + 1)
  else:
    return

for _ in range(k - 1):
  path()

def ans(s, i=0, j=0):

  if i + 1 < n and j + 1 < n:
    if mat[i + 1][j] > mat[i][j + 1]:
      s += "R"
      return ans(s, i, j + 1)
    else:
      s += "D"
      return ans(s, i + 1, j)
  elif i + 1 < n:
    s += "D"
    return ans(s, i + 1, j)
  elif j + 1 < n:
    s += "R"
    return ans(s, i, j + 1)
  return s

print(ans("", 0, 0))