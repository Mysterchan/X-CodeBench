import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        long[] K = new long[N];

        Map<Integer, Integer>[] dice = new HashMap[N];

        for (int i = 0; i < N; i++) {
            dice[i] = new HashMap<>();
            K[i] = sc.nextInt();

            for (int j = 0; j < K[i]; j++) {
                int faceValue = sc.nextInt();

                dice[i].put(faceValue, dice[i].getOrDefault(faceValue, 0) + 1);
            }
        }
        sc.close();

        double maxProb = 0.0;

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {

                long totalOutcomes = K[i] * K[j];

                long sumOfProducts = 0;

                Map<Integer, Integer> die1 = dice[i];
                Map<Integer, Integer> die2 = dice[j];

                if (die1.size() > die2.size()) {

                    Map<Integer, Integer> temp = die1;
                    die1 = die2;
                    die2 = temp;
                }

                for (Map.Entry<Integer, Integer> entry : die1.entrySet()) {
                    int v = entry.getKey();
                    long count_i = entry.getValue();

                    long count_j = die2.getOrDefault(v, 0);

                    sumOfProducts += count_i * count_j;
                }

                double currentProb = (double) sumOfProducts / totalOutcomes;

                maxProb = Math.max(maxProb, currentProb);
            }
        }

        System.out.printf("%.15f\n", maxProb);
    }
}