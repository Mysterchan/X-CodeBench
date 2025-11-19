def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    xor_values = set()
    
    # Generate all partitions using bitmask representation
    # We'll use a recursive approach to generate partitions
    def generate_partitions(bags, current_partition):
        if not bags:
            # Calculate XOR for this partition
            xor_val = 0
            for group in current_partition:
                group_sum = sum(a[i] for i in group)
                xor_val ^= group_sum
            xor_values.add(xor_val)
            return
        
        # Take the first bag
        first_bag = bags[0]
        remaining = bags[1:]
        
        # Add to existing groups
        for i in range(len(current_partition)):
            new_partition = [group.copy() for group in current_partition]
            new_partition[i].append(first_bag)
            generate_partitions(remaining, new_partition)
        
        # Create new group
        new_partition = [group.copy() for group in current_partition]
        new_partition.append([first_bag])
        generate_partitions(remaining, new_partition)
    
    generate_partitions(list(range(n)), [])
    
    print(len(xor_values))

solve()