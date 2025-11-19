import java.util.Scanner;
import java.util.Arrays;

public class Main {

    private static boolean isSorted(int[] arr) {
        for (int i = 0; i < 5; i++) {
            if (arr[i] != i + 1) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] A = new int[5];
        for (int i = 0; i < 5; i++) {
            A[i] = sc.nextInt();
        }

        sc.close();

        boolean canBeSorted = false;

        for (int i = 0; i < 4; i++) {

            int[] temp = Arrays.copyOf(A, 5);

            int val = temp[i];
            temp[i] = temp[i+1];
            temp[i+1] = val;

            if (isSorted(temp)) {
                canBeSorted = true;
                break;
            }
        }

        if (canBeSorted) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}