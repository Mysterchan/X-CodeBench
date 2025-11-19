import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        char[][] s = new char[n][n];
        char[][] t = new char[n][n];

        for (int i = 0; i < n; i++) {
            String q = sc.nextLine();
            s[i] = q.toCharArray();
        }
        for (int i = 0; i < n; i++) {
            String q = sc.nextLine();
            t[i] = q.toCharArray();
        }

        int minOperations = Integer.MAX_VALUE;

        // Check for 0, 1, 2, or 3 rotations
        for (int r = 0; r < 4; r++) {
            int changes = calculateChanges(s, t);
            minOperations = Math.min(minOperations, changes + r);
            s = rotateClockwise(s);
        }

        System.out.println(minOperations);
        sc.close();
    }

    public static int calculateChanges(char[][] s, char[][] t) {
        int changes = 0;
        for (int i = 0; i < s.length; i++) {
            for (int j = 0; j < s.length; j++) {
                if (s[i][j] != t[i][j]) {
                    changes++;
                }
            }
        }
        return changes;
    }

    public static char[][] rotateClockwise(char[][] matrix) {
        int n = matrix.length;
        char[][] rotated = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        return rotated;
    }
}