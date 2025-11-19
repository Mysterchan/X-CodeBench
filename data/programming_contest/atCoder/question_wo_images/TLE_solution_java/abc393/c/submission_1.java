import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Set<Set<Integer>> nodes = new HashSet<>();
        int result = 0;

        for(int i = 0; i<m; i++){
            int l = sc.nextInt();
            int r = sc.nextInt();

            if(l == r){
                result++;
            }else{
                Set<Integer> temp = new HashSet<>();
                temp.add(l);
                temp.add(r);
                if(!nodes.add(temp))result++;
            }
        }
        System.out.println(result);
    }
}