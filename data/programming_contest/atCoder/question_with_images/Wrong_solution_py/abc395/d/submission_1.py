N,Q = map(int,input().split())

hato = list(range(N+1))
box = list(range(N+1))
label = list(range(N+1))

for i in range(Q):
    tmp = list(map(int,input().split()))
    a = tmp[1]
    if tmp[0] == 1 or tmp[0] == 2:
        b = tmp[2]

    if tmp[0] == 1:
        hato[a] = box[label[b]]
    elif tmp[0] == 2:
        box[label[a]],box[label[b]] = box[label[b]],box[label[a]]
        label[a],label[b] = label[b],label[a]
    else:
        print(box[hato[a]])