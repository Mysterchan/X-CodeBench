SYSTEM_PROMPT = """
You are an expert Python programmer specializing in competitive programming. Your task is to create input generators for testing programming contest problems. Specifically, you need to implement the following:

1. **corner_test_case_generator()**: This function generates corner or exceptional test cases without using randomness. These cases should target edge scenarios and boundary conditions.
2. **huge_test_case_generator(seed: int = 7)**: This function generates large test cases designed to stress-test the solution's performance. It should focus on maximum input sizes and structured patterns. Use the provided seed for reproducibility.
3. Both functions must return a list of strings, where each string represents a test case formatted as required by the problem statement.
4. Implement a helper function, **_format_case()**, to format and validate the test cases according to the constraints provided in the problem statement.
5. Finally, implement a **main()** function that combines the outputs of both generators into a comprehensive list of test cases.

### Requirements:
- Your program must include the following functions:
  - **corner_test_case_generator**
  - **huge_test_case_generator**
  - **_format_case**
  - **main**
- Ensure that all test cases strictly adhere to the constraints and formatting rules specified in the problem statement.

Write your code enclosed in a Python code block, and ensure it is well-structured and easy to understand.
"""

USER_PROMPT_1 = """
You are given the following programming problem:
You are given a length-$N$ integer sequence $A = (A_1, A_2, ..., A_N)$.
Your goal is to perform the following operation repeatedly so that for every length-$L$ contiguous subarray of $A$, the sum is a multiple of $M$.
- Choose an integer $i$ such that $1 ≤ i ≤ N$, and increase the value of $A_i$ by $1$.
Find the minimum possible number of operations before achieving the goal.
Constraints:
- $1 ≤ N, M ≤ 500$
- $1 ≤ L ≤ N$
- $0 ≤ A_i < M$
- All input values are integers.
Input:
The input is given from Standard Input in the following format:
$N$ $M$ $L$
$A_1$ $A_2$ $...$ $A_N$
Output:
Output the answer.
Sample Input 1:
4 5 3
4 2 1 3
Sample Output 1:
4
Explanation:
By performing the operation once choosing $i = 2$, twice choosing $i = 3$, and once choosing $i = 4$, you get $A = (4, 3, 3, 4)$ with a total of four operations, where every length-$3$ contiguous subarray sums to a multiple of $5$.

Construct input generators for this problem as per the requirements mentioned.
"""

ASSISTANT_PROMPT_1 = """
```python
from typing import List
import random


def _format_case(N: int, M: int, L: int, A: List[int]) -> str:
    # Format one test case as the required two-line input string.
    if N < 1 or N > 500:
        raise ValueError("Invalid N")
    if M < 1 or M > 500:
        raise ValueError("Invalid M")
    if L < 1 or L > N:
        raise ValueError("Invalid L")
    if len(A) != N:
        raise ValueError("Array length does not match N")
    for a in A:
        if a < 0 or a >= M:
            raise ValueError("Array element out of bounds")
    return f"{N} {M} {L}\n" + " ".join(str(x) for x in A)


def corner_test_case_generator() -> List[str]:
    # Corner/exceptional test cases without randomness.
    # These target edge behaviors: smallest sizes, L=1 and L=N, M=1 and small M,
    # all-zeros, all-(M-1), alternating patterns, and wrap-around progressions.
    cases = []

    # 1) Trivial smallest and M=1
    cases.append(_format_case(1, 1, 1, [0]))
    cases.append(_format_case(1, 2, 1, [1]))

    # 2) Small N with L=1 vs L=N
    cases.append(_format_case(2, 2, 1, [1, 1]))
    cases.append(_format_case(2, 2, 2, [1, 1]))

    # 3) All equal near M-1, L=1 vs L=N
    cases.append(_format_case(3, 3, 1, [2, 2, 2]))
    cases.append(_format_case(3, 3, 3, [2, 2, 2]))

    # 4) L=N with composite M
    cases.append(_format_case(5, 7, 5, [6, 6, 6, 6, 6]))

    # 5) Alternating high/low with even M
    cases.append(_format_case(6, 6, 3, [0, 5, 0, 5, 0, 5]))

    # More ...

    return cases


def huge_test_case_generator(seed: int = 7) -> List[str]:
    # Large test cases focusing on max sizes to stress performance.
    # N=500 with varied L and both prime/composite M. Includes random-heavy and structured patterns.
    rng = random.Random(seed)
    cases: List[str] = []

    N = 500

    # Helper patterns
    def random_array(M: int) -> List[int]:
        return [rng.randrange(M) for _ in range(N)]

    def alternating(M: int) -> List[int]:
        hi = M - 1
        lo = 0
        return [hi if i % 2 else lo for i in range(N)]

    def periodic(M: int, period: int) -> List[int]:
        base = [i % M for i in range(period)]
        return [base[i % period] for i in range(N)]

    # Composite M=500
    M = 500
    cases.append(_format_case(N, M, 1, random_array(M)))
    cases.append(_format_case(N, M, 2, random_array(M)))
    cases.append(_format_case(N, M, 3, periodic(M, 3)))      # short periodic
    cases.append(_format_case(N, M, 10, periodic(M, 10)))    # longer periodic
    cases.append(_format_case(N, M, 250, random_array(M)))
    cases.append(_format_case(N, M, 499, alternating(M)))
    cases.append(_format_case(N, M, 500, [M - 1] * N))       # all max

    # Prime-like M=499
    M = 499
    cases.append(_format_case(N, M, 1, random_array(M)))
    cases.append(_format_case(N, M, 2, alternating(M)))
    cases.append(_format_case(N, M, 249, random_array(M)))
    cases.append(_format_case(N, M, 498, periodic(M, 6)))
    cases.append(_format_case(N, M, 499, [M - 1] * N))

    # Small M=2 to check parity-heavy behavior at max N
    M = 2
    cases.append(_format_case(N, M, 1, alternating(M)))
    cases.append(_format_case(N, M, 2, alternating(M)))

    return cases


def main() -> List[str]:
    # Combine corner and huge test cases into a comprehensive list.
    return corner_test_case_generator() + huge_test_case_generator()
```
"""

USER_PROMPT_2 = """
You are given the following programming problem:
{problem_statement}
Constraints:
{constraints}
{io_styles}
{samples}
Construct a random input generator. Use the format used in the above example. You can copy the same main function.
"""