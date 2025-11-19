import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt() - 1; // Convert to 0-based index
        }

        long ans = 0;
        int[] lastPosition = new int[N];
        int[] count = new int[N];
        int uniqueCount = 0;

        for (int L = 0; L < N; L++) {
            uniqueCount = 0;
            for (int R = L; R < N; R++) {
                int current = A[R];
                if (count[current] == 0) {
                    uniqueCount++;
                }
                count[current]++;
                
                // The number of operations needed to erase all integers from L to R
                ans += uniqueCount;

                // If we are moving to the next R, we need to adjust the count
                if (R == N - 1 || A[R + 1] != current) {
                    for (int i = L; i <= R; i++) {
                        count[A[i]] = 0; // Reset count for the next L
                    }
                }
            }
        }
        
        System.out.println(ans);
    }
}