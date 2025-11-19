import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

def calculate_max_contests(N, writers):
    max_contests = []
    hells = hard = medium = easy = baby = 0
    
    for a, b, c, d, e in writers:
        hells += a
        hard += b
        medium += c
        easy += d
        baby += e
        
        # Calculate maximum contests that can be held with current writers
        div1 = min(hells, hard, medium)
        div2 = min(hard, medium, easy)
        div3 = min(medium, easy, baby)
        
        max_contests.append(min(div1, div2, div3))
    
    return max_contests

output = []
index = 1
T = int(data[0])
for _ in range(T):
    N = int(data[index])
    index += 1
    writers = []
    
    for i in range(N):
        writers.append(tuple(map(int, data[index].split())))
        index += 1
    
    results = calculate_max_contests(N, writers)
    output.append(" ".join(map(str, results)))

print("\n".join(output))