import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {

        Map<String, String> opposites = new HashMap<>();
        opposites.put("N", "S");
        opposites.put("S", "N");
        opposites.put("E", "W");
        opposites.put("W", "E");
        opposites.put("NE", "SW");
        opposites.put("SW", "NE");
        opposites.put("NW", "SE");
        opposites.put("SE", "NW");

        Scanner sc = new Scanner(System.in);

        String D = sc.next();

        System.out.println(opposites.get(D));

        sc.close();
    }
}