import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        
        long rSquared = (long) r * r;
        long count = 1; // center square
        
        // Count squares in first quadrant (i > 0, j >= 0)
        for (int i = 1; i <= r; i++) {
            // For square at (i, j), farthest corner is (i+0.5, j+0.5)
            // Check (i+0.5)^2 + (j+0.5)^2 <= R^2
            // Using doubled coordinates: (2i+1)^2 + (2j+1)^2 <= 4R^2
            long i2plus1 = 2L * i + 1;
            long i2plus1Squared = i2plus1 * i2plus1;
            
            for (int j = 0; j <= r; j++) {
                long j2plus1 = 2L * j + 1;
                long distSquared = i2plus1Squared + j2plus1 * j2plus1;
                
                if (distSquared <= 4 * rSquared) {
                    count++;
                } else {
                    break; // All further j values will also fail
                }
            }
        }
        
        // Multiply by 4 for all quadrants (excluding axes which are counted separately)
        // Actually, we counted i>0, j>=0, so we have:
        // - Positive i axis and first quadrant
        // We need to account for symmetry properly
        
        // Recount properly: count squares where i>0, j>0, then add axes
        count = 1; // center
        
        // Count i > 0, j > 0
        long quadrantCount = 0;
        for (int i = 1; i <= r; i++) {
            long i2plus1 = 2L * i + 1;
            long i2plus1Squared = i2plus1 * i2plus1;
            
            for (int j = 1; j <= r; j++) {
                long j2plus1 = 2L * j + 1;
                if (i2plus1Squared + j2plus1 * j2plus1 <= 4 * rSquared) {
                    quadrantCount++;
                } else {
                    break;
                }
            }
        }
        
        // Count positive i-axis (j=0, i>0)
        long axisCount = 0;
        for (int i = 1; i <= r; i++) {
            long i2plus1 = 2L * i + 1;
            if (i2plus1 * i2plus1 + 1 <= 4 * rSquared) {
                axisCount++;
            } else {
                break;
            }
        }
        
        // Total: center + 4*quadrant + 4*axis
        count = 1 + 4 * quadrantCount + 4 * axisCount;
        
        System.out.println(count);
    }
}