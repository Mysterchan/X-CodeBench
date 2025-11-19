import java.util.*;

class Main {
    static int[] k;
    static HashMap<Integer, Integer> faceCount[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        k = new int[n];
        faceCount = new HashMap[n];
        
        for (int i = 0; i < n; i++) {
            k[i] = sc.nextInt();
            faceCount[i] = new HashMap<>();
            for (int j = 0; j < k[i]; j++) {
                int faceValue = sc.nextInt();
                faceCount[i].put(faceValue, faceCount[i].getOrDefault(faceValue, 0) + 1);
            }
        }

        double maxProbability = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                double probability = calculateProbability(i, j);
                maxProbability = Math.max(maxProbability, probability);
            }
        }
        System.out.printf("%.12f\n", maxProbability);
    }

    static double calculateProbability(int i1, int i2) {
        int totalPairs = k[i1] * k[i2];
        int sameCount = 0;

        for (Map.Entry<Integer, Integer> entry : faceCount[i1].entrySet()) {
            int faceValue = entry.getKey();
            int countInSecondDie = faceCount[i2].getOrDefault(faceValue, 0);
            sameCount += entry.getValue() * countInSecondDie;
        }

        return (double) sameCount / totalPairs;
    }
}