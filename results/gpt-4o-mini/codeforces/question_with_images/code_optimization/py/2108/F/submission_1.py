import sys

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Create a list to hold the final heights
        final_heights = [0] * n
        
        # Process the towers
        for i in range(n):
            if a[i] > 0:
                # Increment the next a[i] towers
                for j in range(i + 1, min(i + 1 + a[i], n)):
                    final_heights[j] += 1
        
        # Calculate the MEX
        final_heights.sort()
        mex = 0
        for height in final_heights:
            if height == mex:
                mex += 1
            elif height > mex:
                break
        
        results.append(str(mex))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()