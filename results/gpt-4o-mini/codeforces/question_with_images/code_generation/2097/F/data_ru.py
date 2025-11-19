def process_test_case(n, m, initial_suitcases, days):
    lost_suitcases = initial_suitcases[:]
    results = []

    for i in range(m):
        a = days[i][0]
        b = days[i][1]
        c = days[i][2]

        # Calculate the number of suitcases that can be lost in this day's morning check
        found_suitcases = 0
        for j in range(n):
            # Determine previous and next airports in circular manner
            prev_airport = (j - 1) % n
            next_airport = (j + 1) % n

            # Suitcases leave airports
            transfer_to_prev = min(lost_suitcases[j], a[j])
            transfer_to_next = min(lost_suitcases[j], c[j])

            # Update lost suitcases after the transfer
            lost_suitcases[j] -= (transfer_to_prev + transfer_to_next)

            # Check how many can be found
            if lost_suitcases[j] >= b[j]:
                found_suitcases += (lost_suitcases[j] - b[j])

        # Update lost suitcases after transfers
        for j in range(n):
            prev_airport = (j - 1) % n
            next_airport = (j + 1) % n
            lost_suitcases[prev_airport] += min(a[j], lost_suitcases[j])
            lost_suitcases[next_airport] += min(c[j], lost_suitcases[j])

        # Determine remaining lost suitcases
        total_lost = sum(lost_suitcases)
        results.append(total_lost)

    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    outputs = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        initial_suitcases = list(map(int, data[index].split()))
        index += 1
        
        days = []
        for _ in range(m):
            a = list(map(int, data[index].split()))
            index += 1
            b = list(map(int, data[index].split()))
            index += 1
            c = list(map(int, data[index].split()))
            index += 1
            days.append((a, b, c))
        
        result = process_test_case(n, m, initial_suitcases, days)
        outputs.append(" ".join(map(str, result)))
    
    print("\n".join(outputs))

if __name__ == "__main__":
    main()