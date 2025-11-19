import sys
input = sys.stdin.read

def main():
    data = input().split()
    T = int(data[0])
    results = []
    
    idx = 1
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx + 1])
        z = int(data[idx + 2])
        idx += 3
        
        # Check the feasibility of forming the sequence
        n02 = z * 2
        n00 = x + z - n02
        
        if n00 < 0:
            results.append("No")
            continue
        
        # Using up pairs of ones
        pairs_of_ones = y // 2
        
        # We can only have up to y // 2 filled positions to match n00
        if n00 > pairs_of_ones:
            results.append("No")
        else:
            # Now, check if remaining ones can be distributed correctly
            remaining_y = y - (n00 * 2)
            if remaining_y < 0 or remaining_y > z:
                results.append("No")
            else:
                results.append("Yes")

    sys.stdout.write("\n".join(results) + "\n")

main()