import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        l1 = int(data[index])
        r1 = int(data[index + 1])
        l2 = int(data[index + 2])
        r2 = int(data[index + 3])
        index += 4

        count = 0
        
        # Determine the sizes in each direction
        width = r1 - l1
        height = r2 - l2
        
        # Use the concept of counting quadtree nodes required for the rectangular region
        while width > 0 and height > 0:
            # Find the largest power of 2 that fits in both dimensions
            size = 1 << (min(width, height).bit_length() - 1)

            # Each time we can cover a square area of size * size
            count += (width // size) * (height // size)

            # Adjust the remaining dimensions
            if width == size or height == size:
                break
            
            # Now reduce by size in one dimension
            if width > height:
                l1 += size
                width -= size
            else:
                l2 += size
                height -= size
        
        # Add remaining strips to account for any leftover area
        count += width * height
        results.append(str(count))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()