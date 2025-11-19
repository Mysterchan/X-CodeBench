import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for(int i = 0; i < N; i++) {
            A[i] = sc.nextInt() - 1;
        }
        
        long ans = 0;
        
        for(int L = 0; L < N; L++) {
            boolean[] seen = new boolean[N];
            int min = A[L];
            int max = A[L];
            seen[A[L]] = true;
            int segments = 1;
            
            for(int R = L; R < N; R++) {
                int val = A[R];
                
                if(R > L) {
                    if(seen[val]) {
                        // Already seen, no change
                    } else {
                        seen[val] = true;
                        
                        if(val < min) {
                            // Extending to the left
                            if(val == min - 1) {
                                // Connects to existing segment
                            } else {
                                // Creates new segment
                                segments++;
                            }
                            min = val;
                        } else if(val > max) {
                            // Extending to the right
                            if(val == max + 1) {
                                // Connects to existing segment
                            } else {
                                // Creates new segment
                                segments++;
                            }
                            max = val;
                        } else {
                            // val is between min and max
                            boolean leftSeen = (val == min || seen[val - 1]);
                            boolean rightSeen = (val == max || seen[val + 1]);
                            
                            if(leftSeen && rightSeen) {
                                // Merges two segments
                                segments--;
                            } else if(!leftSeen && !rightSeen) {
                                // Creates new segment
                                segments++;
                            }
                            // else: extends one segment, no change
                        }
                    }
                }
                
                ans += segments;
            }
        }
        
        System.out.println(ans);
    }
}