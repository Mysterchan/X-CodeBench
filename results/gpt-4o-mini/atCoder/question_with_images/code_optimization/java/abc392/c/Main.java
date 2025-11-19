import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] P = new int[N];
        int[] Q = new int[N];
        int[] result = new int[N];

        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            Q[i] = sc.nextInt();
        }

        // Create a mapping from person index to bib number
        int[] bibMap = new int[N + 1];
        for (int i = 0; i < N; i++) {
            bibMap[P[i]] = Q[i];
        }

        // Fill the result array based on the staring person
        for (int i = 1; i <= N; i++) {
            result[i - 1] = bibMap[P[i - 1]];
        }

        // Print the result
        System.out.println(Arrays.toString(result).replaceAll("[\\[\\],]", ""));
    }
}