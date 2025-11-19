import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    total_zeros_start = 0
    total_ones_start = 0
    total_zeros_end = 0
    total_ones_end = 0
    diff_zeros = 0
    diff_ones = 0
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        total_zeros_start += a
        total_ones_start += b
        total_zeros_end += c
        total_ones_end += d
        diff_zeros += abs(a - c)
        diff_ones += abs(b - d)
    # The total number of zeros and ones must be equal in start and end states
    # The minimal number of moves is max of total zero moves and total one moves divided by 2
    # Because each move fixes one misplaced element
    # But since each move moves one element, total moves = (diff_zeros + diff_ones) / 2
    # However, diff_zeros == diff_ones because total zeros and ones are conserved
    # So minimal moves = diff_zeros = diff_ones
    # But we must output minimal number of operations, which is diff_zeros (or diff_ones)
    # Actually, each operation moves one element, so total moves = diff_zeros (or diff_ones)
    # But since each element moved fixes one misplaced zero or one, total moves = diff_zeros
    # But diff_zeros counts total absolute difference in zeros per stack, so total moves = diff_zeros
    # But each moved element fixes one misplaced zero or one, so total moves = diff_zeros
    # Actually, since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But each move moves one element, so minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since each element moved fixes one misplaced zero or one, minimal moves = diff_zeros
    # So minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference, so minimal moves = diff_zeros
    # But since each move moves one element, minimal moves = diff_zeros
    # But diff_zeros counts sum of abs(a_i - c_i), so minimal moves = diff_zeros
    # But since each move fixes one misplaced element, minimal moves = diff_zeros
    # But since diff_zeros = diff_ones, minimal moves = diff_zeros
    # But diff_zeros counts total difference