import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int queryNum = Integer.parseInt(sc.next());
        int[] op = new int[queryNum];
        int[] aArray = new int[queryNum];
        int[] bArray = new int[queryNum];
        for (int i = 0; i < queryNum; i++) {
            op[i] = Integer.parseInt(sc.next());
            aArray[i] = Integer.parseInt(sc.next());
            if (op[i] != 3) {
                bArray[i] = Integer.parseInt(sc.next());
            }
        }

        int[] pb = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            pb[i] = i;
        }
        int[] bh = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            bh[i] = i;
        }
        int[] hb = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            hb[i] = i;
        }

        for (int i = 0; i < queryNum; i++) {

            int a = aArray[i];
            int b = bArray[i];

            if (op[i] == 1) {
                pb[a] = b;
            }

            if (op[i] == 2) {
                int v = hb[a];
                int w = hb[b];
                int x = bh[v];
                int y = bh[w];
                hb[a] = w;
                hb[b] = v;
                bh[v] = y;
                bh[w] = x;
            }

            if (op[i] == 3) {
                System.out.println(bh[pb[a]]);
            }
        }

    }
}