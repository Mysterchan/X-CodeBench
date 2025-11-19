import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] p = new int[n];
        int[] q = new int[n];

        for (int i = 0; i < n; i++) {
            p[i] = scanner.nextInt();
        }

        for (int i = 0; i < n; i++) {
            q[i] = scanner.nextInt();
        }

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(q[i], i + 1);
        }

        for (int i = 0; i < n; i++) {
            System.out.print(map.get(p[i]) + " ");
        }
    }
}