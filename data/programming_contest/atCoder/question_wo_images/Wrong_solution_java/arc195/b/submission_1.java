import java.util.*;

public class Main {
    public static boolean canMakeUniformSum(int[] A, int[] B) {
        int N = A.length;
        int targetSum = -1;

        for (int i = 0; i < N; i++) {
            if (A[i] != -1 && B[i] != -1) {
                int currentSum = A[i] + B[i];
                if (targetSum == -1) {
                    targetSum = currentSum;
                } else if (targetSum != currentSum) {
                    return false;
                }
            }
        }

        if (targetSum == -1) targetSum = 0;

        for (int i = 0; i < N; i++) {
            if (A[i] == -1 && B[i] != -1) {
                A[i] = targetSum - B[i];
                if (A[i] < 0) return false;
            } else if (B[i] == -1 && A[i] != -1) {
                B[i] = targetSum - A[i];
                if (B[i] < 0) return false;
            } else if (A[i] == -1 && B[i] == -1) {
                A[i] = 0;
                B[i] = targetSum;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        int[] B = new int[N];

        for (int i = 0; i < N; i++) A[i] = scanner.nextInt();
        for (int i = 0; i < N; i++) B[i] = scanner.nextInt();

        System.out.println(canMakeUniformSum(A, B) ? "Yes" : "No");
        scanner.close();
    }
}