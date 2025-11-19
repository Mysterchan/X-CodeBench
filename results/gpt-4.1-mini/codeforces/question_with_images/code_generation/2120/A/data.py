def can_form_square(l1, b1, l2, b2, l3, b3):
    # The rectangles are given such that l3 ≤ l2 ≤ l1 and b3 ≤ b2 ≤ b1
    # We need to check if these three rectangles can be arranged without rotation
    # to form a perfect square.

    # The total area of the three rectangles must be a perfect square
    total_area = l1 * b1 + l2 * b2 + l3 * b3
    side = int(total_area ** 0.5)
    if side * side != total_area:
        return False

    # Since no rotation allowed, rectangles are placed as is.

    # We try to form the square of side 'side' by placing rectangles in some arrangement.
    # Possible arrangements to check:

    # 1) All three rectangles placed side by side horizontally:
    #    Check if all heights equal side and sum of lengths equal side
    if b1 == b2 == b3 == side and l1 + l2 + l3 == side:
        return True

    # 2) All three rectangles placed vertically:
    #    Check if all lengths equal side and sum of heights equal side
    if l1 == l2 == l3 == side and b1 + b2 + b3 == side:
        return True

    # 3) Place the largest rectangle (l1 x b1) and try to fill the remaining space with the other two
    #    The square side is 'side', so the leftover space is (side - l1) or (side - b1)
    #    We try two main ways:

    # 3a) Place l1 x b1 rectangle at the top, then place the other two rectangles side by side below it
    #     Conditions:
    #     - l1 == side (rectangle spans full width)
    #     - b1 < side (height less than side)
    #     - The other two rectangles placed side by side horizontally must fill the remaining height (side - b1)
    #     - Their lengths must sum to side and their heights must be equal to (side - b1)
    if l1 == side and b1 < side:
        if b2 == b3 == side - b1 and l2 + l3 == side:
            return True

    # 3b) Place l1 x b1 rectangle on the left, then place the other two rectangles stacked vertically on the right
    #     Conditions:
    #     - b1 == side (rectangle spans full height)
    #     - l1 < side (width less than side)
    #     - The other two rectangles stacked vertically must fill the remaining width (side - l1)
    #     - Their heights must sum to side and their lengths must be equal to (side - l1)
    if b1 == side and l1 < side:
        if l2 == l3 == side - l1 and b2 + b3 == side:
            return True

    # No arrangement found
    return False


t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    print("YES" if can_form_square(l1, b1, l2, b2, l3, b3) else "NO")