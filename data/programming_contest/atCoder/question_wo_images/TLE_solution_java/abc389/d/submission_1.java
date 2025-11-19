import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();

        double[] di = {0.5, 0.5, -0.5, -0.5};
        double[] dj = {0.5, -0.5, 0.5, -0.5};
        int count = 0;
        for (int i = 1; i <= r; i++) {
            label:
            for (int j = 0; j <= r; j++) {
                for (int k = 0; k < 4; k++) {
                    double ni = i + di[k];
                    double nj = j + dj[k];
                    double d = Math.sqrt(Math.pow(ni, 2) + Math.pow(nj, 2));
                    if (r < d) continue label;
                }
                count++;
            }
        }
        System.out.println(count * 4 + 1);
    }
}