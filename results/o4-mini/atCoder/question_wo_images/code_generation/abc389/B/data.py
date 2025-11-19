import sys

def main():
    X = int(sys.stdin.readline().strip())
    fact = 1
    i = 1
    
    # Keep multiplying until we match X
    while fact < X:
        i += 1
        fact *= i
    
    # At this point, fact >= X; by problem guarantee, fact == X
    print(i)

if __name__ == "__main__":
    main()