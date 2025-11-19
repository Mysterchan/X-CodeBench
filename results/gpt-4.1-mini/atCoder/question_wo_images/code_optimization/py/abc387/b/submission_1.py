X = int(input())

# Total sum of all 81 cells: sum of i*j for i,j in 1..9
# sum_i=45, total sum = 45*45=2025
total = 2025

# Count how many times X appears in the table
count = 0
for i in range(1, 10):
    if X % i == 0 and 1 <= X // i <= 9:
        count += 1

print(total - count * X)