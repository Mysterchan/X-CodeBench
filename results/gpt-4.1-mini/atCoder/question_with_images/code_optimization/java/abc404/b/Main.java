import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        char[][] S = new char[n][n];
        char[][] T = new char[n][n];
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < n; j++) {
                S[i][j] = line.charAt(j);
            }
        }
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < n; j++) {
                T[i][j] = line.charAt(j);
            }
        }
        sc.close();

        // Precompute all 4 rotations of S
        char[][][] rotations = new char[4][][];
        rotations[0] = S;
        for (int r = 1; r < 4; r++) {
            rotations[r] = rotateClockwise(rotations[r - 1], n);
        }

        int minOps = Integer.MAX_VALUE;
        // For each rotation, count the number of differing cells
        for (int r = 0; r < 4; r++) {
            int diff = 0;
            char[][] rotated = rotations[r];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (rotated[i][j] != T[i][j]) diff++;
                }
            }
            // Total operations = number of rotations + number of flips
            // rotations cost r operations (each 90 degree rotation)
            // flips cost diff operations (each cell flip)
            int ops = r + diff;
            if (ops < minOps) minOps = ops;
        }

        System.out.println(minOps);
    }

    private static char[][] rotateClockwise(char[][] matrix, int n) {
        char[][] rotated = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        return rotated;
    }
}