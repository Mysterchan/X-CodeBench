from collections import deque
import sys
input = sys.stdin.read


def main():
    data = input().strip().splitlines()
    Q = int(data[0])
    queries = data[1:]

    queue = deque()
    head_adjustment = 0
    results = []

    for query in queries:
        parts = query.split()
        type_of_query = int(parts[0])

        if type_of_query == 1:  # Add snake
            length = int(parts[1])
            # Calculate the actual head position considering adjustments
            if not queue:  # If the queue is empty
                head_position = 0
            else:  # Get the last snake's head position and add its length
                last_snake_length = queue[-1][1]
                last_snake_head = queue[-1][0] + last_snake_length
                head_position = last_snake_head
            
            # Append the new snake (head position, length)
            queue.append((head_position, length))

        elif type_of_query == 2:  # Remove the front snake
            removed_length = queue.popleft()[1]  # Get the length of the removed snake
            head_adjustment += removed_length  # Adjust the global offset of all remaining snakes

        elif type_of_query == 3:  # Query head position of k-th snake
            k = int(parts[1]) - 1  # Convert to zero-indexed
            actual_head_index = queue[k][0] - head_adjustment  # Calculate actual head position
            results.append(actual_head_index)

    # Print all results for type 3 queries
    sys.stdout.write('\n'.join(map(str, results)) + '\n')


if __name__ == "__main__":
    main()