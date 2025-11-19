N = int(input())
A = list(map(int, input().split()))

# Count how many A_i are odd
odd_count = sum(a % 2 for a in A)

# If the count of odd numbers is odd, Fennec wins; otherwise, Snuke wins
print("Fennec" if odd_count % 2 == 1 else "Snuke")