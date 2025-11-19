import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        // Store frequency maps for each die
        Map<Integer, Integer>[] freqMaps = new HashMap[n];
        int[] k = new int[n];
        
        for (int i = 0; i < n; i++) {
            k[i] = sc.nextInt();
            freqMaps[i] = new HashMap<>();
            for (int j = 0; j < k[i]; j++) {
                int val = sc.nextInt();
                freqMaps[i].put(val, freqMaps[i].getOrDefault(val, 0) + 1);
            }
        }

        double max = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int same = 0;
                // Iterate over common keys only
                for (Map.Entry<Integer, Integer> entry : freqMaps[i].entrySet()) {
                    int num = entry.getKey();
                    if (freqMaps[j].containsKey(num)) {
                        same += entry.getValue() * freqMaps[j].get(num);
                    }
                }
                int all = k[i] * k[j];
                max = Math.max(max, (double) same / all);
            }
        }
        System.out.println(max);
    }
}