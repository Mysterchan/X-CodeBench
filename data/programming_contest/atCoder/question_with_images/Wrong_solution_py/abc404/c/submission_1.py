def main():
  N, M = map(int, input().split())
  edges = []
  for _ in range(M):
    row = list(map(int, input().split()))
    edges.append(row)

  vertexes = [0]*N

  for i in range(M):
    vertexes[edges[i][0]-1] += 1
    vertexes[edges[i][1]-1] += 1

  ans = 'Yes'
  for vertex in vertexes:
    if vertex != 2:
      ans = 'No'
      break
  print(ans)

if __name__ == "__main__":
  main()