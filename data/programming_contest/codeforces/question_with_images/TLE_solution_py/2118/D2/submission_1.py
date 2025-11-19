def process_traffic_lights(test_cases):
    results = []

    for n, k, positions, delays, queries in test_cases:
        lights = {}

        for p, d in zip(positions, delays):
            lights[p] = d

        for a in queries:
            current_position = a
            direction = 1

            for _ in range(10**100):
                if current_position in lights:
                    delay = lights[current_position]
                    time = (10**100) % k

                    if time == delay or (time > delay and (time - delay) % k == 0):
                        direction *= -1

                current_position += direction

                if current_position < 1 or current_position > 10**15:
                    results.append("YES")
                    break
            else:
                results.append("NO")

    return results


t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))
    delays = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))
    test_cases.append((n, k, positions, delays, queries))

results = process_traffic_lights(test_cases)

for result in results:
    print(result)
