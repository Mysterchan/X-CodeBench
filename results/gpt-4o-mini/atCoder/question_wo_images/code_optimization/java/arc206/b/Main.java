import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] power = new int[n];
        int[] color = new int[n];
        for (int i = 0; i < n; i++)
            power[i] = scanner.nextInt();
        for (int i = 0; i < n; i++)
            color[i] = scanner.nextInt();

        // To store positions of each power's original position
        int[] originalPos = new int[n + 1];
        for (int i = 0; i < n; i++) {
            originalPos[power[i]] = i;
        }

        // Store colors in the order of the size (power)
        int[][] colorGroups = new int[n + 1][];
        for (int col = 1; col <= n; col++) {
            List<Integer> tempList = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (color[i] == col)
                    tempList.add(power[i]);
            }
            colorGroups[col] = new int[tempList.size()];
            for (int i = 0; i < tempList.size(); i++) {
                colorGroups[col][i] = tempList.get(i);
            }
        }

        long totalCost = 0L;

        for (int col = 1; col <= n; col++) {
            if (colorGroups[col].length == 0) continue;
            int[] sequence = colorGroups[col];
            Arrays.sort(sequence);

            // Find the minimum number of changes required
            int maxLength = 0;
            int[] dp = new int[sequence.length];
            for (int i = 0; i < sequence.length; i++) {
                int currentPower = sequence[i];
                int positionInOriginal = originalPos[currentPower];
                int predMaxLength = 0;
                for (int j = 0; j < i; j++) {
                    if (originalPos[sequence[j]] < positionInOriginal) {
                        predMaxLength = Math.max(predMaxLength, dp[j]);
                    }
                }
                dp[i] = predMaxLength + 1;
                maxLength = Math.max(maxLength, dp[i]);
            }

            int size = sequence.length;
            totalCost += (long) (size - maxLength) * col;
        }

        System.out.println(totalCost);
    }
}