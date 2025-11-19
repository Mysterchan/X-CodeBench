import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        char[][] S = new char[N][N];
        for (int i = 0; i < N; i++) {
            S[i] = sc.next().toCharArray();
        }

        char[][] T = new char[M][M];
        for (int i = 0; i < M; i++) {
            T[i] = sc.next().toCharArray();
        }

        for (int r = 0; r <= N - M; r++) {
            for (int c = 0; c <= N - M; c++) {

                boolean isMatch = true;

                for (int i_t = 0; i_t < M; i_t++) {
                    for (int j_t = 0; j_t < M; j_t++) {

                        if (S[r + i_t][c + j_t] != T[i_t][j_t]) {

                            isMatch = false;
                            break;
                        }
                    }
                    if (!isMatch) {
                        break;
                    }
                }

                if (isMatch) {

                    int a = r + 1;
                    int b = c + 1;
                    System.out.println(a + " " + b);

                    sc.close();
                    return;
                }
            }
        }

        sc.close();
    }
}