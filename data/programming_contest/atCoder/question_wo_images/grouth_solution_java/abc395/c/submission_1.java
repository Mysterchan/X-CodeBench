import java.util.*;
import java.util.stream.*;
import java.math.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashSet<Integer> judge = new HashSet<>();
        int score = 0;
        int ans = -1;
        for (int i = 0; i < n; i++){
            int A = sc.nextInt();
            if(judge.contains(A)){
                score = i - map1.get(A) + 1;
                map1.put(A,i);
                if(ans == -1) ans = score;
                else ans = Math.min(ans,score);
            }else{
                map1.put(A,i);
                judge.add(A);
            }
        }
        System.out.println(ans);
    }

}