def max_unfound_luggage(t, test_cases):
    results = []
    for case in test_cases:
        n, m, s, days = case
        
        # Results for this test case
        unfound_results = []
        
        for i in range(m):
            # Day-specific data
            a = days[i][0]
            b = days[i][1]
            c = days[i][2]
            
            # Current state of luggage at airports
            s_current = s[:]
            
            # Calculate how many luggage pieces can be sent, found, and remain unfound
            # Migrate luggage to previous airports
            for j in range(n):
                index_prev = (j - 1) % n
                send_to_prev = min(s_current[j], a[j])
                s_current[j] -= send_to_prev
                s_current[index_prev] += send_to_prev
            
            # Migrate luggage to next airports
            for j in range(n):
                index_next = (j + 1) % n
                send_to_next = min(s_current[j], c[j])
                s_current[j] -= send_to_next
                s_current[index_next] += send_to_next
            
            # Check for found luggage
            for j in range(n):
                if s_current[j] >= b[j]:
                    s_current[j] -= (s_current[j] - b[j])
            
            # Calculate total unfound luggage
            total_unfound = sum(s_current)
            unfound_results.append(total_unfound)
            s = s_current  # Update luggage state for the next day's calculations
        
        results.append(unfound_results)
    
    return results


# Reading input and processing
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    t = int(data[index])  # Number of test cases
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        s = list(map(int, data[index].split()))
        index += 1
        
        days = []
        for __ in range(m):
            a = list(map(int, data[index].split()))
            index += 1
            b = list(map(int, data[index].split()))
            index += 1
            c = list(map(int, data[index].split()))
            index += 1
            days.append((a, b, c))
        
        result = max_unfound_luggage(t, [(n, m, s, days)])
        results.append(result[0])
    
    for res in results:
        print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()