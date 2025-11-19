n,q = map(int,input().split())

P = [1]*(n+1)

count = set()

for _ in range(q):

    query = list(map(int,input().split()))

    if query[0] == 2:

        print(len(count))

    else:

        p,h = query[1],query[2]

        P[h] += P[p]
        P[p] = 0

        if P[h] >= 2:

            count.add(h)

        count.discard(p)