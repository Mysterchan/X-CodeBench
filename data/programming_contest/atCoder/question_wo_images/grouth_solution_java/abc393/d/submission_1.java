import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        sc.close();

        ArrayList<Long> p = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (S.charAt(i) == '1') {
                p.add((long) i);
            }
        }

        int K = p.size();

        ArrayList<Long> b = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            b.add(p.get(i) - i);
        }

        Collections.sort(b);

        long median;
        if (K % 2 == 1) {
            median = b.get(K / 2);
        } else {

            median = b.get(K / 2);
        }

        long totalSwaps = 0;
        for (int i = 0; i < K; i++) {
            totalSwaps += Math.abs(b.get(i) - median);
        }

        System.out.println(totalSwaps);
    }
}