import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        boolean[] exists = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            exists[a] = true;
        }

        sc.close();

        List<Integer> missing = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            if (!exists[i]) {
                missing.add(i);
            }
        }

        System.out.println(missing.size());

        if (missing.size() > 0) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < missing.size(); i++) {
                sb.append(missing.get(i));
                if (i < missing.size() - 1) {
                    sb.append(" ");
                }
            }
            System.out.println(sb.toString());
        }
    }
}