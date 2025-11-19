import sys
input = sys.stdin.readline

Q = int(input())

# We'll maintain a queue of snakes, each represented by (head_coordinate, length).
# Instead of updating all head coordinates on type 2 queries, we keep a global offset.
# When a snake leaves, we increase offset by its length.
# When adding a snake, its head coordinate is last_snake_head + last_snake_length.
# When querying, we output stored_head_coordinate - offset.

snakes = []
offset = 0
front = 0  # index of the front snake in the list

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        l = int(query[1])
        if front == len(snakes):
            # queue empty
            head = 0
        else:
            last_head, last_len = snakes[-1]
            head = last_head + last_len
        snakes.append((head, l))
    elif t == 2:
        # snake at front leaves
        head, length = snakes[front]
        offset += length
        front += 1
    else:
        k = int(query[1])
        head, length = snakes[front + k - 1]
        print(head - offset)