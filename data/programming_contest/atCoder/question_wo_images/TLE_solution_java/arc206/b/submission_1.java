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
        ArrayList<Integer>[] groupedByColor = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++)
            groupedByColor[i] = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            groupedByColor[color[i]].add(power[i]);
        }
        long totalCost = 0L;
        for (int col = 1; col <= n; col++) {
            ArrayList<Integer> sequence = groupedByColor[col];
            int size = sequence.size();
            if (size == 0) continue;
            ArrayList<Integer> lisTails = new ArrayList<>();
            for (int value : sequence) {
                int position = lowerBound(lisTails, value);
                if (position == lisTails.size())
                    lisTails.add(value);
                else
                    lisTails.set(position, value);
            }
            int lisLength = lisTails.size();
            totalCost += (long) (size - lisLength) * col;
        }
        System.out.println(totalCost);
    }

    private static int lowerBound(ArrayList<Integer> list, int key) {
        int low = 0, high = list.size();
        while (low < high) {
            int mid = (low + high) / 2;
            if (list.get(mid) >= key)
                high = mid;
        }
        return low;
    }
}