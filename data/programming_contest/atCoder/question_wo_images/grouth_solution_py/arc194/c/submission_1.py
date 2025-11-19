n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

idx = sorted(range(n), key=lambda i: -c[i])
a = [a[i] for i in idx]
b = [b[i] for i in idx]
c = [c[i] for i in idx]

suf_a = [0] * (n + 1)
suf_b = [0] * (n + 1)
for i in range(n - 1, -1, -1):
  suf_a[i] = suf_a[i + 1] + a[i] * c[i]
  suf_b[i] = suf_b[i + 1] + b[i] * c[i]

off_first = [0] * (n + 1)
for i in range(n):
  off_first[i + 1] = off_first[i]
  if a[i] == 1:
    off_first[i + 1] += suf_a[i + 1]
turn_again = 0
cnt = 0
for i in range(n):
  if b[i] == 1:
    cnt += 1
    turn_again += cnt * c[i]
  off_first[i + 1] += turn_again + cnt * suf_b[i + 1]

correct_suf = [0] * (n + 1)
cnt = 0
for i in range(n - 1, -1, -1):
  correct_suf[i] = correct_suf[i + 1]
  if a[i] == 1 and b[i] == 0:
    correct_suf[i] += suf_a[i + 1]
    cnt += 1
  if a[i] == 0 and b[i] == 1:
    correct_suf[i] += suf_b[i]
    cnt += 1
  if a[i] == 1 and b[i] == 1:
    correct_suf[i] += cnt * c[i]

print(min(a + b for a, b in zip(off_first, correct_suf)))