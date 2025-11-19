import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        Map<Integer, String> InputMap = new HashMap<>();
        for(int i = 0; i < num; i++){
            String word = sc.next();
            int length = word.length();

            InputMap.put(length, word);

        }

        for(Integer key:InputMap.keySet()){
            String ans = InputMap.get(key);
            System.out.print(ans);
        }

    }
}