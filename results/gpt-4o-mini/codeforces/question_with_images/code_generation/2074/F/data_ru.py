def count_nodes(l1, r1, l2, r2):
    # Calculate the size of the area
    width = r1 - l1
    height = r2 - l2
    
    # Calculate the number of nodes needed
    nodes = 0
    while width > 0 or height > 0:
        # Determine the largest power of 2 that fits in the current width and height
        size = 1
        while size <= width or size <= height:
            size *= 2
        size //= 2
        
        # Count how many full squares of this size fit in the area
        nodes += ((width + size - 1) // size) * ((height + size - 1) // size)
        
        # Reduce the area
        width -= size
        height -= size
    
    return nodes

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        l1, r1, l2, r2 = map(int, data[i].split())
        result = count_nodes(l1, r1, l2, r2)
        results.append(result)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()