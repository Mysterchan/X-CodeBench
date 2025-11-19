N = int(input())
A = list(map(int, input().split()))

total = sum(A)
cnt_even = sum(1 for x in A if x % 2 == 0)

# The winner is determined by the parity after optimal play
# Players will try to control parity by choosing when to activate odd indices
if (total - cnt_even) % 2 == 1:
    print("Fennec")
else:
    print("Snuke")