def min_nodes_to_cover_area(l1, r1, l2, r2):
    # Calculate the width and height of the area
    width = r1 - l1
    height = r2 - l2
    
    # Calculate the number of nodes needed in each dimension
    nodes_width = (width + 1) // 2  # Each node covers 2 units in width
    nodes_height = (height + 1) // 2  # Each node covers 2 units in height
    
    # Total nodes needed is the product of nodes in width and height
    return nodes_width * nodes_height

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        l1, r1, l2, r2 = map(int, data[i].split())
        result = min_nodes_to_cover_area(l1, r1, l2, r2)
        results.append(result)
    
    # Print all results for each test case
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()