import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class Main {
    static int N;
    static long[] A;
    static Set<Long> results;

    static void dfs(int index, List<Long> currentSums) {

        if (index == N) {
            long xorSum = 0;

            for (long sum : currentSums) {
                xorSum ^= sum;
            }
            results.add(xorSum);
            return;
        }

        long element = A[index];

        for (int i = 0; i < currentSums.size(); i++) {
            long oldSum = currentSums.get(i);

            currentSums.set(i, oldSum + element);

            dfs(index + 1, currentSums);

            currentSums.set(i, oldSum);
        }

        currentSums.add(element);

        dfs(index + 1, currentSums);

        currentSums.remove(currentSums.size() - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        results = new HashSet<>();

        dfs(0, new ArrayList<Long>());

        System.out.println(results.size());

        sc.close();
    }
}