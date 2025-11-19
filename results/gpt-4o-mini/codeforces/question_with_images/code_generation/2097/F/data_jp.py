def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        
        s = list(map(int, data[index].split()))
        index += 1
        
        max_unfound = []
        
        for day in range(m):
            a = list(map(int, data[index].split()))
            index += 1
            b = list(map(int, data[index].split()))
            index += 1
            c = list(map(int, data[index].split()))
            index += 1
            
            # Calculate the lost luggage after this day
            new_s = s[:]
            for j in range(n):
                prev_airport = (j - 1 + n) % n
                next_airport = (j + 1) % n
                
                # Transport from prev_airport to j
                transported_from_prev = min(a[j], new_s[prev_airport])
                new_s[prev_airport] -= transported_from_prev
                
                # Transport from next_airport to j
                transported_from_next = min(c[j], new_s[next_airport])
                new_s[next_airport] -= transported_from_next
            
            # Count how many are unfound
            unfound = 0
            for j in range(n):
                if new_s[j] >= b[j]:
                    unfound += new_s[j] - b[j]
            
            # Store the result for the current day
            max_unfound.append(unfound)
            s = new_s  # Update s for next day

        results.append(max_unfound)
    
    # Print final results for all test cases
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()