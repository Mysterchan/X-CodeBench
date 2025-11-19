import java.util.*;
import java.util.stream.*;
import java.math.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> nokori = new HashMap<>();
        HashSet<Integer> nice = new HashSet<>();
        for (int i = 1; i <= n; i++){
            map1.put(i,i);
            nokori.put(i,1);
        }
        for (int i = 0; i < q; i++){
            int judge = sc.nextInt();
            if(judge == 1){
                int p = sc.nextInt();
                int h = sc.nextInt();
                int bhome = map1.get(p);
                map1.put(p,h);
                nokori.put(bhome,nokori.get(bhome)-1);
                nokori.put(h,nokori.getOrDefault(h,0)+1);
                if(nokori.get(h) >= 2) nice.add(h);
                if(nokori.get(bhome) < 2) nice.remove(bhome);
            }
            if(judge == 2){
                System.out.println(nice.size());
            }
        }
    }

}