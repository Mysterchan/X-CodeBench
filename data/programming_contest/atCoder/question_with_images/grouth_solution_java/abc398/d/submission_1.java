import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int R = sc.nextInt();
        int C = sc.nextInt();
        String S = sc.next();

        Set<String> set = new HashSet<>();
        int fireR = 0;
        int fireC = 0;
        set.add("0_0");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            char c = S.charAt(i);
            if (c == 'E') {
                fireC--;
            } else if (c == 'W') {
                fireC++;
            } else if (c == 'S') {
                fireR--;
            } else if (c == 'N') {
                fireR++;
            }
            set.add(fireR + "_" + fireC);
            sb.append(set.contains((fireR + R) + "_" + (fireC + C)) ? 1 : 0);
        }
        System.out.println(sb.toString());
    }
}