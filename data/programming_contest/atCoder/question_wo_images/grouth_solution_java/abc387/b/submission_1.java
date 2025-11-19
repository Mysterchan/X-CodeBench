import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int X = scanner.nextInt();

        int totalSum = 0;

        for (int i = 1; i <= 9; i++) {

            for (int j = 1; j <= 9; j++) {

                int cellValue = i * j;

                if (cellValue != X) {

                    totalSum += cellValue;
                }
            }
        }

        System.out.println(totalSum);

        scanner.close();
    }
}