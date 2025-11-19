import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] p = Arrays.stream(new int[n]).map(e -> sc.nextInt()).toArray();
        int[] c = Arrays.stream(new int[n]).map(e -> sc.nextInt()).toArray();

        Vector<Integer>[] vectors = new Vector[n + 1];

        for(int i = 1; i <= n; i++) {
            vectors[i] = new Vector();
        }

        for(int i = 0; i < n; i++) {
            vectors[c[i]].add(p[i]);
        }

        long result = 0;
        for(int i = 1; i <= n; i++) {
            result += (long)i * (vectors[i].size() - LIS(vectors[i]));
        }

        System.out.println(result);

    }

    static int LIS (Vector<Integer> vec) {
        int[] dp = new int[vec.size()];
        Arrays.fill(dp, Integer.MAX_VALUE);

        for(int i = 0; i < vec.size(); i++) {
            int index = lowerBound(dp, vec.get(i));
            dp[index] = vec.get(i);
        }

        return lowerBound(dp, Integer.MAX_VALUE);
    }

    static int lowerBound(int[] array, int key) {
        int index = Arrays.binarySearch(array, key);

        if (index >= 0) {
            while(index > 0) {
                if(array[index - 1] == key) {
                    index--;
                }
                else {
                    break;
                }
            }
        }
        else {
            index++;
            index *= -1;
        }

        return index;
    }

}