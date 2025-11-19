Looking at this problem, I need to:

1. Maintain a set S of positive integers, starting with all positive integers
2. For each query with parameters A_i and B_i:
   - Remove all multiples of A_i from S
   - Find and print the B_i-th smallest element in S

The key challenge is that S is infinite, so I can't store all elements. Instead, I need to:
- Keep track of which numbers to exclude (multiples of various A_i values seen so far)
- When finding the B_i-th smallest element, generate candidates efficiently

My approach:
1. Maintain a set of "forbidden" values (A_i that we've seen)
2. When we need the B_i-th smallest element, iterate through positive integers and count those that aren't multiples of any forbidden value
3. Return the B_i-th such number

Let me trace through the example:
- Initially S = {1,2,3,4,5,6,7,8,9,10,...}
- Query 1: A=5, B=10. Remove multiples of 5. S = {1,2,3,4,6,7,8,9,11,12,...}. 10th element is 12 ✓
- Query 2: A=6, B=1. Remove multiples of 6. S = {1,2,3,4,7,8,9,11,13,14,...}. 1st element is 1 ✓
- Query 3: A=6, B=10. Already removed multiples of 6. S = {1,2,3,4,7,8,9,11,13,14,...}. 10th element is 14 ✓[View your solution](computer:///mnt/user-data/outputs/solution.py)