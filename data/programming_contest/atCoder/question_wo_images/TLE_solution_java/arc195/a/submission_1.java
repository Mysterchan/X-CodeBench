import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            Map<Integer, List<Integer>> aMap = new HashMap<>();
            for (int i = 0; i < n; i++) {
                int num = sc.nextInt();
                List<Integer> list = aMap.getOrDefault(num, new ArrayList<>());
                list.add(i);
                aMap.put(num, list);
            }
            List<List<Integer>> listList = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                int num = sc.nextInt();
                if (!aMap.containsKey(num))
                    break;
                listList.add(aMap.get(num));
            }

            if (listList.size() < m) {
                System.out.println("No");
                return;
            }

            int[] minSubsequence = new int[m];
            int[] maxSubsequence = new int[m];
            List<Integer> firstList = listList.get(0);
            minSubsequence[0] = firstList.get(0);
            List<Integer> lastList = listList.get(listList.size() - 1);
            maxSubsequence[m - 1] = lastList.get(lastList.size() - 1);

            for (int i = 1; i < m; i++) {
                int prev = minSubsequence[i - 1];
                List<Integer> list = listList.get(i);
                Integer[] listArray = list.stream().toArray(Integer[]::new);
                int index = Arrays.binarySearch(listArray, prev);
                index = index < 0 ? ~index : index + 1;
                if (index >= listArray.length) {
                    System.out.println("No");
                    return;
                }
                minSubsequence[i] = listArray[index];
            }

            for (int i = m - 2; i >= 0; i--) {
                int next = maxSubsequence[i + 1];
                List<Integer> list = listList.get(i);
                Integer[] listArray = list.stream().toArray(Integer[]::new);
                int index = Arrays.binarySearch(listArray, next);
                index = index < 0 ? ~index - 1 : index - 1;
                if (index < 0) {
                    System.out.println("No");
                    return;
                }
                maxSubsequence[i] = listArray[index];
            }

            for (int i = 0; i < m; i++) {
                if (minSubsequence[i] != maxSubsequence[i]) {
                    System.out.println("Yes");
                    return;
                }
            }

            System.out.println("No");
        }
    }
}