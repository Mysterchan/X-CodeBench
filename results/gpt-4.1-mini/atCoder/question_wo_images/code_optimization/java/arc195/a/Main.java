import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    // Custom binary search to find the smallest element > key
    private static int upperBound(List<Integer> list, int key) {
        int low = 0, high = list.size();
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (list.get(mid) <= key) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    // Custom binary search to find the largest element < key
    private static int lowerBound(List<Integer> list, int key) {
        int low = 0, high = list.size();
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (list.get(mid) < key) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low - 1;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            // Read A and store positions for each value
            // Using a HashMap is still efficient, but we avoid repeated boxing/unboxing by using primitive int arrays
            // However, since values can be large, we keep HashMap<Integer, List<Integer>>
            // But we avoid repeated toArray calls by working directly on lists

            // Map from value to list of positions (sorted)
            java.util.HashMap<Integer, List<Integer>> posMap = new java.util.HashMap<>();
            for (int i = 0; i < n; i++) {
                int val = sc.nextInt();
                posMap.computeIfAbsent(val, k -> new ArrayList<>()).add(i);
            }

            int[] B = new int[m];
            List<List<Integer>> posLists = new ArrayList<>(m);
            boolean possible = true;
            for (int i = 0; i < m; i++) {
                B[i] = sc.nextInt();
                List<Integer> list = posMap.get(B[i]);
                if (list == null) {
                    possible = false;
                }
                posLists.add(list);
            }

            if (!possible) {
                System.out.println("No");
                return;
            }

            int[] minSeq = new int[m];
            int[] maxSeq = new int[m];

            // Build minSeq: earliest subsequence matching B
            // minSeq[0] = first occurrence of B[0]
            minSeq[0] = posLists.get(0).get(0);
            for (int i = 1; i < m; i++) {
                List<Integer> currList = posLists.get(i);
                int idx = upperBound(currList, minSeq[i - 1]);
                if (idx == currList.size()) {
                    System.out.println("No");
                    return;
                }
                minSeq[i] = currList.get(idx);
            }

            // Build maxSeq: latest subsequence matching B
            // maxSeq[m-1] = last occurrence of B[m-1]
            List<Integer> lastList = posLists.get(m - 1);
            maxSeq[m - 1] = lastList.get(lastList.size() - 1);
            for (int i = m - 2; i >= 0; i--) {
                List<Integer> currList = posLists.get(i);
                int idx = lowerBound(currList, maxSeq[i + 1]);
                if (idx < 0) {
                    System.out.println("No");
                    return;
                }
                maxSeq[i] = currList.get(idx);
            }

            // Check if minSeq and maxSeq differ at any position
            for (int i = 0; i < m; i++) {
                if (minSeq[i] != maxSeq[i]) {
                    System.out.println("Yes");
                    return;
                }
            }

            System.out.println("No");
        }
    }
}