import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); // Read number of test cases
        StringBuilder output = new StringBuilder();

        for (int t = 0; t < T; t++) {
            int H = scanner.nextInt();
            int W = scanner.nextInt();
            String S = scanner.next();
            
            // Calculate the numbers of D's and R's in S
            int dCount = 0, rCount = 0, wildcardCount = 0;
            for (char c : S.toCharArray()) {
                if (c == 'D') dCount++;
                else if (c == 'R') rCount++;
                else wildcardCount++;
            }
            
            // Calculate remaining D's and R's that can be used
            int remainingD = (H - 1) - dCount; // Maximum D's we can use
            int remainingR = (W - 1) - rCount; // Maximum R's we can use

            // The maximum extra cells we can cover with wildcards are the ones we can fill with remaining Ds or Rs
            int totalMoves = H + W - 2; // Total number of moves
            if (remainingD < 0 || remainingR < 0 || (remainingD + remainingR) > wildcardCount) {
                output.append(0).append("\n"); // No valid path can be formed
            } else {
                output.append(H + W - 1).append("\n"); // Max cells painted black
            }
        }
        
        System.out.print(output.toString()); // Output result for all test cases
        scanner.close();
    }
}