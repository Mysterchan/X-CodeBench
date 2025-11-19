import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())

# Храним уже проведённые отрезки в виде интервалов [l, r]
# Отрезки не пересекаются, поэтому интервалы не пересекаются.
# Для проверки пересечения нового отрезка [l, r] с уже проведёнными:
# - Найдём позицию вставки по l
# - Проверим интервал слева и справа на пересечение

intervals = []  # список кортежей (l, r), отсортирован по l

for _ in range(Q):
    A, B = map(int, input().split())
    l, r = A, B
    # l < r гарантируется по условию
    # Проверяем пересечения с уже проведёнными отрезками
    pos = bisect.bisect_left(intervals, (l, r))
    conflict = False
    # Проверяем интервал слева
    if pos > 0:
        L, R = intervals[pos - 1]
        if R > l:
            conflict = True
    # Проверяем интервал справа
    if not conflict and pos < len(intervals):
        L, R = intervals[pos]
        if L < r:
            conflict = True
    if conflict:
        print("No")
    else:
        print("Yes")
        intervals.insert(pos, (l, r))