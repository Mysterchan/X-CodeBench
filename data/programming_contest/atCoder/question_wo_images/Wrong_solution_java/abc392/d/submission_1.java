import java.util.*;

class Main {
    static Map<Integer, Integer>[] maps;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] k = new int[n];
        int[][] a = new int[n][];
        for (int i = 0; i < n; i++) {
            k[i] = sc.nextInt();
            a[i] = new int[k[i]];
            for (int j = 0; j < k[i]; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        maps = new HashMap[n];
        for (int i = 0; i < n; i++) {
            maps[i] = new HashMap<>();
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k[i]; j++) {
                maps[i].put(a[i][j], maps[i].getOrDefault(a[i][j], 0) + 1);
            }
        }

        double max = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int all = k[i] * k[j];
                int same = getSame(i, j);
                max = Math.max(max, (double) same / all);
            }
        }
        System.out.println(max);
    }

    static int getSame(int i1, int i2) {
        int count = 0;
        for (var key : maps[i1].keySet()) {
            if (maps[i2].containsKey(key)) {
                count += maps[i1].get(key) * maps[i2].get(key);
            }
        }
        return count;
    }
}