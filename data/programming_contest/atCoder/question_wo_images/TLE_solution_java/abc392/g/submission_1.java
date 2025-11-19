import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] S = new int[N];
        int maxVal = 0;
        for (int i = 0; i < N; i++) {
            S[i] = sc.nextInt();
            maxVal = Math.max(maxVal, S[i]);
        }

        sc.close();

        boolean[] exists = new boolean[maxVal + 1];
        for (int val : S) {
            exists[val] = true;
        }

        long count = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int A = S[i];
                int C = S[j];

                if (A >= C) {
                    continue;
                }

                if ((A + C) % 2 == 0) {
                    int B = (A + C) / 2;

                    if (exists[B]) {
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}