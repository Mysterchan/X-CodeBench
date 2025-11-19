import sys

def solve():
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
        
        for day in range(m):
            a = list(map(int, data[index].split()))
            index += 1
            b = list(map(int, data[index].split()))
            index += 1
            c = list(map(int, data[index].split()))
            index += 1
            
            new_s = [0] * n
            
            for j in range(n):
                # Calculate luggage after flights
                prev_airport = (j - 1) % n
                next_airport = (j + 1) % n
                
                # Luggage sent to previous airport
                sent_to_prev = min(s[j], a[j])
                # Luggage sent to next airport
                sent_to_next = min(s[j] - sent_to_prev, c[j])
                
                # Remaining luggage after sending
                remaining = s[j] - (sent_to_prev + sent_to_next)
                
                # Luggage found
                found = max(0, remaining - b[j])
                
                # Update new luggage count
                new_s[prev_airport] += sent_to_prev
                new_s[next_airport] += sent_to_next
                new_s[j] = remaining - found
            
            s = new_s
            results.append(sum(s))
    
    sys.stdout.write(" ".join(map(str, results)) + "\n")

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()