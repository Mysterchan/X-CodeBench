import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] A = new int[5];
        for (int i = 0; i < 5; i++) {
            A[i] = sc.nextInt();
        }

        sc.close();

        int adjacentInversions = 0;

        for (int i = 0; i < 4; i++) {
            if (A[i] > A[i+1]) {
                adjacentInversions++;
            }
        }

        if (adjacentInversions == 1) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}