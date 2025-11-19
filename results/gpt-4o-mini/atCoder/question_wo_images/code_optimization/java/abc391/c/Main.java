import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        
        int[] nests = new int[n + 1]; // To count pigeons in each nest
        int countMoreThanOne = 0; // To keep track of nests with more than one pigeon
        
        // Initialize each pigeon in its own nest
        for (int i = 1; i <= n; i++) {
            nests[i] = 1; // Each nest starts with one pigeon
        }
        
        // Process each query
        for (int i = 0; i < q; i++) {
            int type = sc.nextInt();
            if (type == 1) {
                int p = sc.nextInt();
                int h = sc.nextInt();
                
                // Move pigeon p from its current nest to nest h
                int currentNest = p; // Pigeon p is initially in nest p
                nests[currentNest]--; // Remove pigeon from its current nest
                
                // Check if the current nest now has less than 2 pigeons
                if (nests[currentNest] == 1) {
                    countMoreThanOne--; // It had 2, now it has 1
                }
                
                nests[h]++; // Add pigeon to nest h
                
                // Check if the new nest now has 2 pigeons
                if (nests[h] == 2) {
                    countMoreThanOne++; // It now has 2
                }
            } else if (type == 2) {
                // Output the number of nests with more than one pigeon
                System.out.println(countMoreThanOne);
            }
        }
    }
}