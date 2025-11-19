import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            A[i] = scanner.nextInt();
        }

        long[] stones = new long[N + 1];
        System.arraycopy(A, 0, stones, 0, N + 1);
        
        // Track how many adults currently have stones
        long adultsWithStones = 0;
        
        for (int i = 1; i <= N; i++) {
            // Alien i becomes adult at year i
            // They receive stones from all current adults with stones
            stones[i] += adultsWithStones;
            
            // Calculate how many times this alien will give stones
            // They give to aliens i+1, i+2, ..., N (total N-i aliens)
            // But only while they have stones
            long yearsRemaining = N - i;
            long timesGive = Math.min(stones[i], yearsRemaining);
            
            // Update stones after giving
            stones[i] -= timesGive;
            
            // If this alien still has stones after all giving, they count as adult with stones
            if (stones[i] > 0) {
                adultsWithStones++;
            }
        }
        
        for (int i = 1; i <= N; i++) {
            System.out.print(stones[i]);
            if (i < N) System.out.print(" ");
        }
        System.out.println();
    }
}