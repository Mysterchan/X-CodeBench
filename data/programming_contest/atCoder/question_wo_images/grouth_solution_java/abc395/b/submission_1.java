import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.close();

        char[][] grid = new char[N][N];

        for (int i = 1; i <= N; i++) {

            int j = N + 1 - i;

            if (i > j) {
                break;
            }

            char color = (i % 2 == 1) ? '#' : '.';

            int r1 = i - 1;
            int c1 = i - 1;
            int r2 = j - 1;
            int c2 = j - 1;

            for (int r = r1; r <= r2; r++) {
                for (int c = c1; c <= c2; c++) {
                    grid[r][c] = color;
                }
            }
        }

        for (int r = 0; r < N; r++) {

            System.out.println(new String(grid[r]));
        }
    }
}