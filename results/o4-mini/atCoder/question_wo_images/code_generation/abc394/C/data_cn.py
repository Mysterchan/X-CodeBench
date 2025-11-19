import sys
import threading

def main():
    S = list(sys.stdin.readline().rstrip())
    n = len(S)
    i = 0
    # Scan through S, replacing leftmost "WA" with "AC" and backtracking one step after each replacement
    while i < n - 1:
        if S[i] == 'W' and S[i+1] == 'A':
            # Perform replacement
            S[i], S[i+1] = 'A', 'C'
            # Step back to catch any newly formed "WA" just before
            if i > 0:
                i -= 1
        else:
            i += 1
    # Output the final string
    sys.stdout.write(''.join(S))

if __name__ == "__main__":
    threading.Thread(target=main).start()