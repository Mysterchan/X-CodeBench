import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int R = sc.nextInt();
        int C = sc.nextInt();
        String S = sc.next();
        
        // Current position of smoke
        int smokeR = 0, smokeC = 0;
        // To track if smoke exists at (R, C) at time t + 0.5
        StringBuilder result = new StringBuilder();
        
        // Set to track smoke positions
        Set<String> smokePositions = new HashSet<>();
        smokePositions.add("0,0"); // Initial smoke position
        
        for (int i = 0; i < N; i++) {
            char direction = S.charAt(i);
            // Move smoke based on the direction
            if (direction == 'N') {
                smokeR--;
            } else if (direction == 'S') {
                smokeR++;
            } else if (direction == 'E') {
                smokeC++;
            } else if (direction == 'W') {
                smokeC--;
            }
            
            // Check if smoke exists at (R, C) at time t + 0.5
            if (smokePositions.contains(R + "," + C)) {
                result.append('1');
            } else {
                result.append('0');
            }
            
            // Update smoke positions
            smokePositions.add(smokeR + "," + smokeC);
        }
        
        // Final check for the last position
        if (smokePositions.contains(R + "," + C)) {
            result.append('1');
        } else {
            result.append('0');
        }
        
        System.out.println(result.toString());
    }
}