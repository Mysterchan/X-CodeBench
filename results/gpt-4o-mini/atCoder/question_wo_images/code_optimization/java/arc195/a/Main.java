import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            Map<Integer, Integer> lastIndexMap = new HashMap<>();
            boolean subsequenceFound = false;

            // Read sequence A and track last seen positions of elements
            for (int i = 0; i < n; i++) {
                int num = sc.nextInt();
                lastIndexMap.put(num, i);
            }
            
            // Read sequence B and check for the subsequence
            int lastIndex = -1;
            for (int i = 0; i < m; i++) {
                int bNum = sc.nextInt();
                if (!lastIndexMap.containsKey(bNum)) {
                    System.out.println("No");
                    return;
                }
                int currentIndex = lastIndexMap.get(bNum);
                if (currentIndex <= lastIndex) {
                    subsequenceFound = true;
                    break;
                }
                lastIndex = currentIndex;               
            }

            // If we found a subsequence, we want to check if we can find it again
            if (subsequenceFound) {
                // Reset last seen index for the second check and ensure we can find it
                lastIndex = -1;
                for (int i = 0; i < m; i++) {
                    int bNum = sc.nextInt();
                    if (lastIndexMap.containsKey(bNum)) {
                        int currentIndex = lastIndexMap.get(bNum);
                        if (currentIndex <= lastIndex) { // found the subsequence again
                            System.out.println("Yes");
                            return;
                        }
                        lastIndex = currentIndex;
                    }
                }
            }

            System.out.println("No");
        }
    }
}