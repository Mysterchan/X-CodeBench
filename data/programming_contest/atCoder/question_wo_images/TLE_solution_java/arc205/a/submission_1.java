import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int q = sc.nextInt();

        char[][] matrix = new char[n][n];

        for(int i = 0; i < n; i++) {
            matrix[i] = sc.next().toCharArray();
        }

        for(int i = 0; i < q; i++) {
            solve(matrix, sc.nextInt() - 1, sc.nextInt() - 1, sc.nextInt() - 1, sc.nextInt() - 1);
        }
    }

    static void solve(char matrix[][], int u, int d, int l, int r) {
        char[][] matrixClone = matrix.clone();

        int count = 0;
        for(int i = u; i <= d - 1; i++) {
            for(int j = l; j <= r - 1; j++) {
                boolean isOk = true;
                for(int k = 0; k < 2; k++) {
                    for(int p = 0; p < 2; p++) {
                        if(matrixClone[i + k][j + p] == '#') {
                            isOk = false;
                            break;
                        }
                    }
                }

                if(isOk) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}