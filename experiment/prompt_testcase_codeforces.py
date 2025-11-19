SYSTEM_PROMPT = """
You are an expert python competitive programmar and your goal is to construct input-test-case-generators for testing programming contest problems.
You have to write two relevant generators:
1) corner_test_case_generator(t: int) -> str: This function generates corner/exceptional test cases.
2) huge_test_case_generator(t: int) -> str: This function randomly generates large test cases focusing on max sizes to stress performance.

In each test-trial, either corner_test_case_generator or huge_test_case_generator will be called with an integer t representing the number of test cases to generate.
Therefore, both functions should accept an integer parameter t and return a single string representing the test case formatted as required.
e.g you can see something like this:
# Input:
#   t
#     n_1
#     l_1 r_1
#     ...
#     l_n r_n
#     n_2
#     x_1 y_1
#     ...
#     x_n y_n
#     ...
#     n_t
#     a_1 b_1
#     ...
#     a_n b_n

On the other hand, you need to generate some helper functions to format the test cases correctly and validate the constraints.
3) a _format_case function should be used to format the test cases correctly and validate the constraints.
4) Finally, write a main() function that randomly calls either corner_test_case_generator or huge_test_case_generator, with a random integer t, and returns a comprehensive list of test cases.

Your program should at least contains
1) corner_test_case_generator function,
2) huge_test_case_generator function,
3) _format_case function,
4) main function

Remember to strictly follow the instructions and constraints present in the problem statement and Write your code enclosed in a ```python``` block.
"""

USER_PROMPT_1 = """
You are given the following programming problem:
Roaming through the alligator-infested Everglades, Florida Man encounters a most peculiar showdown.
There are $n$ lilypads arranged in a row, numbered from $1$ to $n$ from left to right.
Alice and Bob are frogs initially positioned on distinct lilypads, $a$ and $b$, respectively.
They take turns jumping, starting with Alice.
During a frog's turn, it can jump either one space to the left or one space to the right, as long as the destination lilypad exists.
For example, on Alice's first turn, she can jump to either lilypad $a-1$ or $a+1$, provided these lilypads are within bounds.
It is important to note that each frog must jump during its turn and cannot remain on the same lilypad.
However, there are some restrictions: 
- The two frogs cannot occupy the same lilypad. 
This means that Alice cannot jump to a lilypad that Bob is currently occupying, and vice versa. 
- If a frog cannot make a valid jump on its turn, it loses the game. As a result, the other frog wins.
Determine whether Alice can guarantee a win, assuming that both players play optimally.
It can be proven that the game will end after a finite number of moves if both players play optimally.

Constraints:
Input
Each test contains multiple test cases. 
The first line contains the number of test cases $t$ ($1 ≤ t ≤ 10^4$). 
The description of the test cases follows.
The first line of each test case contains a single integer $n$ ($1≤ n≤ 2 \cdot 10^5$)
— the number of rows of the polyomino.\nThe $i$-th of the next $n$ lines contains two integers $l_i$ and $r_i$ ($1≤ l_i≤ r_i≤ 10^9$)
— the range of columns that are part of the polyomino in the $i$-th row.
It is guaranteed that the area of the polyomino is even. 
In other words, $\\sum_{i=1}^n r_i - l_i + 1\\equiv 0\\pmod{2}$.
It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \\cdot 10^5$.
Output\nFor each test case, print a single line containing either \"YES\" or \"NO\", representing whether or not the polyomino can be partitioned as described in the problem.
You can output the answer in any case (upper or lower). For example, the strings \"yEs\", \"yes\", \"Yes\", and \"YES\" will be recognized as positive responses.

For example, the following is one of the expected output from the generator function when t=5:
Sample Input 1:
5
2 1 2
3 3 1
4 2 3
5 2 4
7 6 2

Construct input generators for this problem as per the requirements mentioned.
"""

ASSISTANT_PROMPT_1 = """
```python
import random
from typing import List, Tuple

# We follow the sample format:
# t
# n a b
# n a b
# ...
# Constraints enforced here:
# 1 <= t <= 1e4
# 2 <= n <= 1e9
# 1 <= a, b <= n and a != b

T_MAX = 10_000
N_MIN = 2
N_MAX = 1_000_000_000

def _format_case(cases: List[Tuple[int, int, int]]) -> str:
    "
    Validate and format cases as a single string.
    Each case is a tuple: (n, a, b)
    "
    t = len(cases)
    if not (1 <= t <= T_MAX):
        raise ValueError(f"t must be in [1, {T_MAX}], got {t}")
    out = [str(t)]
    for idx, (n, a, b) in enumerate(cases, start=1):
        if not (isinstance(n, int) and isinstance(a, int) and isinstance(b, int)):
            raise TypeError(f"All values must be integers in case #{idx}")
        if not (N_MIN <= n <= N_MAX):
            raise ValueError(f"n out of bounds in case #{idx}: {n}")
        if not (1 <= a <= n and 1 <= b <= n):
            raise ValueError(f"a,b must be within [1, n] in case #{idx}: a={a}, b={b}, n={n}")
        if a == b:
            raise ValueError(f"a and b must be distinct in case #{idx}: a={a}, b={b}")
        out.append(f\"{n} {a} {b}\")
    return \"\\n\".join(out)

def corner_test_case_generator(t: int) -> str:
    "
    Generate edge/corner scenarios for the frog game:
    - Minimal n
    - Frogs at ends, adjacent, near edges
    - Mixed small/medium n
    "
    base_cases: List[Tuple[int, int, int]] = [
        (2, 1, 2),     # minimal, ends
        (2, 2, 1),     # minimal, swapped
        (3, 1, 2),     # near left edge, adjacent
        (3, 2, 3),     # near right edge, adjacent
        (3, 1, 3),     # ends
        (4, 2, 3),     # middle adjacent
        (5, 1, 5),     # ends
        (5, 2, 4),     # symmetric middle
        (5, 3, 4),     # adjacent middle-right
        (6, 1, 2),     # adjacent at left
        (6, 5, 6),     # adjacent at right
        (10, 1, 10),   # larger ends
        (10, 4, 7),    # mid spread
        (10, 5, 6),    # center adjacent
    ]
    if t <= len(base_cases):
        cases = base_cases[:t]
    else:
        cases = list(base_cases)
        rng = random.Random()
        while len(cases) < t:
            n = rng.choice([2, 3, 4, 5, 10, 11, 20, 100, 1_000, 10_000])
            if n < 2:
                n = 2
            # Create varied corner-like placements
            mode = rng.randint(0, 4)
            if mode == 0:
                a, b = 1, n
            elif mode == 1:
                a = rng.randint(1, n - 1)
                b = a + 1
            elif mode == 2:
                a = rng.randint(2, n)
                b = a - 1
            elif mode == 3:
                a = rng.randint(1, min(n, 5))
                b = rng.randint(max(1, n - 4), n)
                if a == b:
                    b = n if a != n else 1
            else:
                a = rng.randint(1, n)
                b = rng.randint(1, n - 1)
                if b >= a:
                    b += 1
            cases.append((n, a, b))
    return _format_case(cases)

def huge_test_case_generator(t: int) -> str:
    "
    Generate large random cases focusing on max sizes to stress performance.
    "
    rng = random.Random()
    big_pool = [N_MAX, N_MAX - 1, N_MAX - 2, 10**9 - 123, 10**8, 10**7, 10**6]
    cases: List[Tuple[int, int, int]] = []
    for _ in range(t):
        n = rng.choice(big_pool)
        if n < 2:
            n = 2
        r = rng.random()
        if r < 0.20:
            a, b = 1, n
        elif r < 0.40:
            a, b = n, 1
        elif r < 0.60:
            # Adjacent near edges
            if rng.random() < 0.5:
                a, b = 1, 2
            else:
                a, b = n - 1, n
        elif r < 0.80:
            # Adjacent somewhere random
            a = rng.randint(1, n - 1)
            b = a + 1
        else:
            # Two distinct random positions
            a = rng.randint(1, n)
            b = rng.randint(1, n - 1)
            if b >= a:
                b += 1
        cases.append((n, a, b))
    return _format_case(cases)

def main() -> str:
    "
    Randomly choose generator and t, and return the test set as a string.
    You can reuse this main for other problems by swapping the generator functions.
    "
    rng = random.Random()
    # Keep output size practical while valid per constraints
    t = rng.randint(1, min(200, T_MAX))
    generator = rng.choice([corner_test_case_generator, huge_test_case_generator])
    return generator(t)

if __name__ == "__main__":
    print(main())
```
```
"""

USER_PROMPT_2 = """
You are given the following programming problem:
{problem_statement}
Constraints:
{io_styles}
For example, the following is one of the expected output from the generator function when:
{samples}

Construct a random input generator. Use the format used in the above example. You can copy the same main function.
"""