import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] ratingChanges = new int[500001]; // To store the number of contests affecting each rating

        // Read the contests and mark the ranges
        for (int i = 0; i < n; i++) {
            int l = s.nextInt();
            int r = s.nextInt();
            ratingChanges[l]++;
            if (r + 1 < ratingChanges.length) {
                ratingChanges[r + 1]--;
            }
        }

        // Calculate the cumulative number of contests affecting each rating
        for (int i = 1; i < ratingChanges.length; i++) {
            ratingChanges[i] += ratingChanges[i - 1];
        }

        int q = s.nextInt();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int x = s.nextInt();
            output.append(x + ratingChanges[x]).append("\n");
        }

        System.out.print(output);
    }
}