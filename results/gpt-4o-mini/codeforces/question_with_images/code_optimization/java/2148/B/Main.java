import java.util.*;
public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        StringBuilder result = new StringBuilder();
        
        while(t-- > 0){
            int n = sc.nextInt();
            int m = sc.nextInt();
            int x = sc.nextInt();
            int y = sc.nextInt();

            Set<Integer> horizontalLasers = new HashSet<>();
            for(int i = 0; i < n; i++){
                horizontalLasers.add(sc.nextInt());
            }

            Set<Integer> verticalLasers = new HashSet<>();
            for(int i = 0; i < m; i++){
                verticalLasers.add(sc.nextInt());
            }

            int crossings = 0;
            if (horizontalLasers.size() > 0 && !horizontalLasers.contains(y)) {
                crossings++;
            }
            if (verticalLasers.size() > 0 && !verticalLasers.contains(x)) {
                crossings++;
            }
            crossings += horizontalLasers.size() + verticalLasers.size(); 

            result.append(crossings).append("\n");
        }
        
        System.out.print(result);
    }
}