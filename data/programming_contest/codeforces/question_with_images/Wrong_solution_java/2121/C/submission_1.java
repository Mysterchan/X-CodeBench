import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        while (t-- > 0) {

            int n = in.nextInt();
            int m = in.nextInt();
            int[][] a = new int[n][m];
            int max = 0;
            int r = 0, c = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    a[i][j] = in.nextInt();
                    if (a[i][j] > max) {
                        max = a[i][j];
                        r = i;
                        c = j;
                    }
                }
            }

            HashMap<Integer, Integer> row = new HashMap<>();
            HashMap<Integer, Integer> col = new HashMap<>();
            ArrayList<int[]> list = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (a[i][j] == max) {
                        if (row.containsKey(i)) r = i;
                        if (col.containsKey(j)) c = j;
                        row.put(i, 1);
                        col.put(j, 1);
                        list.add(new int[]{i, j});
                    }
                }
            }


            if (list.size() <= 2) {
                System.out.println(max - 1);
            }
            else if (list.size() == 3) {
                boolean flag = false;


                int[] x = new int[n];
                int[] y = new int[m];

                for (int i = 0; i < list.size(); i++) {
                    int R = list.get(i)[0];
                    int C = list.get(i)[1];


                    if (x[R] == 1 || y[C] == 1) {
                        flag = true;
                    }
                    x[R]++;
                    y[C]++;
                }

                if (flag) {
                    System.out.println(max - 1);
                } else {
                    System.out.println(max);
                }
            }
            else {
                boolean flag = true;
                for (int i = 0; i < list.size(); i++) {
                    int R = list.get(i)[0];
                    int C = list.get(i)[1];
                    if (R != r && C != c) {
                        flag = false;
                        break;
                    }
                }

                if (!flag) {
                    System.out.println(max);
                } else {
                    System.out.println(max - 1);
                }
            }
        }
    }
}
