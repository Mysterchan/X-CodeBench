import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] k = new int[n];
        // Use array of HashMaps to store frequency of each face per die
        HashMap<Integer, Integer>[] freq = new HashMap[n];
        for (int i = 0; i < n; i++) {
            k[i] = sc.nextInt();
            freq[i] = new HashMap<>();
            for (int j = 0; j < k[i]; j++) {
                int face = sc.nextInt();
                freq[i].put(face, freq[i].getOrDefault(face, 0) + 1);
            }
        }

        double maxProb = 0.0;
        // For each pair of dice, compute sum of freq_i[x]*freq_j[x]
        for (int i = 0; i < n - 1; i++) {
            HashMap<Integer, Integer> mapI = freq[i];
            for (int j = i + 1; j < n; j++) {
                HashMap<Integer, Integer> mapJ = freq[j];
                // Iterate over smaller map for efficiency
                if (mapI.size() > mapJ.size()) {
                    HashMap<Integer, Integer> temp = mapI;
                    mapI = mapJ;
                    mapJ = temp;
                }
                long sameCount = 0;
                for (Map.Entry<Integer, Integer> entry : mapI.entrySet()) {
                    int face = entry.getKey();
                    int countI = entry.getValue();
                    Integer countJ = mapJ.get(face);
                    if (countJ != null) {
                        sameCount += (long) countI * countJ;
                    }
                }
                double prob = (double) sameCount / (k[i] * (long) k[j]);
                if (prob > maxProb) maxProb = prob;
            }
        }

        System.out.println(maxProb);
    }
}