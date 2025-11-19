import java.util.*;

class Main {
    static int[] k;
    static int[][] a;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        k = new int[n];
        a = new int[n][];
        for (int i = 0; i < n; i++) {
            k[i] = sc.nextInt();
            a[i] = new int[k[i]];
            for (int j = 0; j < k[i]; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        double max = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int same = getSame(i, j);
                int all = k[i] * k[j];
                max = Math.max(max, (double) same / all);
            }
        }
        System.out.println(max);
    }

    static int getSame(int i1, int i2) {
        int count = 0;
        for (int j1 = 0; j1 < k[i1]; j1++) {
            for (int j2 = 0; j2 < k[i2]; j2++) {
                if (a[i1][j1] == a[i2][j2]) count++;
            }
        }
        return count;
    }
}