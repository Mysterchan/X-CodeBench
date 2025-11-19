import java.util.Scanner;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        HashSet<Integer> S = new HashSet<>();

        for (int i = 0; i < N; i++) {
            S.add(sc.nextInt());
        }

        sc.close();
        long count = 0;

        for (int val : S) {
            for (int otherVal : S) {
                if (val >= otherVal) {
                    continue;
                }
                
                int A = val;
                int C = otherVal;
                int B = (A + C) / 2;
                
                if ((A + C) % 2 == 0 && S.contains(B)) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}