import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        if(n != m){
            System.out.println("No");
            return;
        }
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        for(int i = 0;i < m;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(!map.containsKey(a)){
                List<Integer> lst = new ArrayList<>();
                map.put(a, lst);
            }
            if(map.get(a).size() == 2 || map.get(a).contains(b)){
                System.out.println("No");
                return;
            }
            map.get(a).add(b);
            if(!map.containsKey(b)){
                List<Integer> lst = new ArrayList<>();
                map.put(b, lst);
            }
            if(map.get(b).size() == 2 || map.get(b).contains(a)){
                System.out.println("No");
                return;
            }
            map.get(b).add(a);
        }
        List<Integer> all = new ArrayList<>();
        int cur = 1;
        for(int i = 0;i < n;i++){
            List<Integer> lst = map.get(cur);
            if(!all.contains(lst.get(0))){
                cur = lst.get(0);
                all.add(lst.get(0));
            } else if(!all.contains(lst.get(1))){
                cur = lst.get(1);
                all.add(lst.get(1));
            } else {
                System.out.println("No");
                return;
            }
        }
        if(all.size() == n){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        br.close();
    }
}